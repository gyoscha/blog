from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms


class SignUp(CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('rest_framework:login')
    template_name = "registration/signup.html"
