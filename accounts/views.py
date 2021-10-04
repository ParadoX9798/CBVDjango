from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy


class UserLogin(LoginView):
    template_name = "accounts/login.html"


class PasswordReset(PasswordResetView):
    template_name = "accounts/password_reset_form.html"
    success_url = reverse_lazy("accounts:password_reset_done")
    email_template_name = "accounts/password_reset_email.html"


class PasswordResetDone(PasswordResetDoneView):
    template_name = "accounts/reset_done.html"


class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"
    success_url = reverse_lazy("accounts:password_reset_complete")


class PasswordResetComplete(PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"
