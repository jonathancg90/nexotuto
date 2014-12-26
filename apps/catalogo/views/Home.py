# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.contrib import auth, messages
from django.conf import settings
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, FormView
from django.http import HttpResponseRedirect
from django.views.generic.base import RedirectView

from apps.catalogo.forms.UserForm import LoginForm
from apps.catalogo.forms.UserForm import SignUpForm


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        data = form.clean()

        user = auth.authenticate(
            username=data.get('username', ''),
            password=data.get('password', '')
        )
        if user is not None:
            auth.login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            messages.error(self.request, 'Incorrect login or password.')
            return self.form_invalid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        return super(LoginView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('home')


class SignUpView(CreateView):
    model = User
    template_name = 'sign_up.html'
    form_class = SignUpForm

    def form_valid(self, form):
        data = form.clean()
        user = form.save(commit=False)
        user.set_password(data.get('password'))
        return super(SignUpView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        return super(SignUpView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('home')

class LogoutView(RedirectView):
    url = settings.LOGIN_URL

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)