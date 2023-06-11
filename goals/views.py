from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from accounts.models import CustomUser
from goals.models import Goals
from accounts.fit_scores import scores


class GoalUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Goals
    fields = (
        "goal_type",
        "title",
        "description",
        "estimated_finish_date"
    )
    template_name = "goal_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class GoalDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Goals
    template_name = "goal_delete.html"
    success_url = reverse_lazy("goalslist")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def form_valid(self, form):
        if self.object.status == "Active":
            user = CustomUser.objects.get(username=self.request.user)
            user.active_goals -= 1
            user.save()
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class GoalCreateView(LoginRequiredMixin, CreateView):
    model = Goals
    template_name = "goal_new.html"
    fields = ("goal_type", "title", "description", "estimated_finish_date")

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(GoalCreateView, self).get_form(form_class)
        form.fields['estimated_finish_date'].widget = forms.TextInput(attrs={'placeholder': 'Accepted format: MM/DD/YYYY'})
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        user = CustomUser.objects.get(username=self.request.user)
        user.active_goals += 1
        user.fit_points += scores["newgoal"]
        user.save()
        return super().form_valid(form)


class GoalListView(LoginRequiredMixin, ListView):
    model = Goals
    template_name = "goals_list.html"

    ordering = ['status']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["today_date"] = timezone.now().date()
        return context


class GoalCompleteView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Goals
    template_name = "goal_complete.html"
    fields = ()

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def form_valid(self, request, *args, **kwargs):
        user = CustomUser.objects.get(username=self.request.user)
        user.active_goals -= 1
        user.completed_goals += 1
        user.fit_points += scores["goalcomplete"]
        user.save()
        obj = self.get_object()
        obj.status = "Completed"
        obj.complete_date = timezone.now().date()
        obj.save()
        return HttpResponseRedirect(reverse_lazy("goalslist"))

