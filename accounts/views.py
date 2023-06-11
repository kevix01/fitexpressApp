from django.urls import reverse_lazy
from django.views.generic import CreateView
from django import forms
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(SignUpView, self).get_form(form_class)
        form.fields['birth'].widget = forms.TextInput(attrs={'placeholder': 'Accepted format: MM/DD/YYYY'})
        return form
