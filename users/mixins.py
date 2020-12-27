from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.urls.base import reverse_lazy


class EmailLoginOnlyView(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.login_method == "email"

    def handle_no_permission(self):
        messages.error(self.request, _("Can't go there"))
        return redirect(reverse("core:home"))


class LoggedOutOnlyView(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, _("Can't go there"))
        return redirect(reverse("core:home"))


class LoggedInOnlyView(LoginRequiredMixin):
    login_url = reverse_lazy("users:login")
