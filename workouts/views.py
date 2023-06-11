from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # new
from django import forms
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from accounts.models import CustomUser
from .models import Workout, WorkoutExercises, Exercises
from accounts.fit_scores import scores


class WorkoutListView(LoginRequiredMixin, ListView):
    model = Workout
    template_name = "workout_list.html"
    ordering = ['-last_training_date']


class WorkoutStandardListView(LoginRequiredMixin, ListView):
    model = Workout
    template_name = "workoutstandard_list.html"


class WorkoutUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Workout
    fields = (
        "title",
        "description",
    )
    template_name = "workout_edit.html"

    def test_func(self):  # new
        obj = self.get_object()
        return obj.author == self.request.user

    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponseRedirect(reverse_lazy("workoutlist"))


class WorkoutTrainView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Workout
    fields = ()
    template_name = "workout_train.html"
    success_url = reverse_lazy("workoutlist")

    def test_func(self):  # new
        obj = self.get_object()
        return obj.author == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["exercises"] = WorkoutExercises.objects.filter(workout=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        if form.instance.author == "FitExpress":
            form.instance.last_training_date = timezone.now().date()
        user = CustomUser.objects.get(username=self.request.user)
        user.fit_points += scores["workoutcomplete"]
        user.calories_burned += self.object.kcal
        user.save()
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class WorkoutExerciseCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = WorkoutExercises
    fields = (
        "exercise",
        "repetitions",
    )
    template_name = "workoutexercise_new.html"

    def test_func(self):  # new
        obj = Workout.objects.get(pk=self.kwargs["pk"])
        return obj.author == self.request.user

    def form_valid(self, form):  # new
        form.instance.workout = Workout.objects.get(pk=self.kwargs["pk"])
        form.instance.workout.exercise_num += 1
        form.instance.kcal_tot = form.instance.exercise.kcal_rep * form.instance.repetitions
        form.instance.workout.kcal += form.instance.kcal_tot
        form.instance.workout.save()
        super().form_valid(form)
        return HttpResponseRedirect(reverse_lazy('workoutexercises', kwargs={'workout_pk': form.instance.workout.pk}))

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(WorkoutExerciseCreateView, self).get_form(form_class)
        form.fields['exercise'] = forms.ModelChoiceField(
            queryset=Exercises.objects.all().order_by('muscle_group')
        )
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workout"] = Workout.objects.get(pk=self.kwargs["pk"])
        return context


class WorkoutExercisesView(LoginRequiredMixin, ListView):
    model = WorkoutExercises
    template_name = "workoutexercises_list.html"
    context_object_name = "workoutexercises"

    def get_queryset(self):
        query = super().get_queryset()
        workout = Workout.objects.get(pk=self.kwargs["workout_pk"])
        qs = query.filter(workout=workout)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workout"] = Workout.objects.get(pk=self.kwargs["workout_pk"])
        return context


class WorkoutExerciseEdit(LoginRequiredMixin, UpdateView):
    model = WorkoutExercises
    fields = (
        "exercise",
        "repetitions",
    )
    template_name = "workoutexercise_edit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workout"] = Workout.objects.get(pk=self.kwargs["workout_pk"])
        return context

    def form_valid(self, form):
        form.instance.workout.kcal -= self.object.kcal_tot
        form.instance.kcal_tot = form.instance.exercise.kcal_rep * form.instance.repetitions
        form.instance.workout.kcal += form.instance.kcal_tot
        form.instance.workout.save()
        return super().form_valid(form)


class WorkoutExerciseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # new
    model = WorkoutExercises
    template_name = "workoutexercise_delete.html"
    success_url = reverse_lazy("workoutexercises")

    def get_success_url(self):
        return reverse_lazy('workoutexercises', kwargs={'workout_pk': self.kwargs['workout_pk']})

    def test_func(self):
        obj = Workout.objects.get(pk=self.kwargs["workout_pk"])
        return obj.author == self.request.user

    def form_valid(self, form):
        workout = Workout.objects.get(pk=self.kwargs["workout_pk"])
        workout.exercise_num -= 1
        workout.kcal -= self.object.kcal_tot
        workout.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workout"] = Workout.objects.get(pk=self.kwargs["workout_pk"])
        return context


class WorkoutDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Workout
    template_name = "workout_delete.html"
    success_url = reverse_lazy("workoutlist")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def delete(self, request, *args, **kwargs):
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class WorkoutCreateView(LoginRequiredMixin, CreateView):
    model = Workout
    template_name = "workout_new.html"
    fields = ("title", "description")

    def form_valid(self, form):
        form.instance.author = self.request.user
        user = CustomUser.objects.get(username=self.request.user)
        user.fit_points += scores["newworkout"]
        user.save()
        return super().form_valid(form)
