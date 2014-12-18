from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from accounts.forms import PasswordResetForm, UpdatePasswordForm

#------------------------------------------------------------
# Forgot Password
#------------------------------------------------------------

class PasswordResetView(FormView):
    form_class = PasswordResetForm
    template_name = "registration/password_reset.html"

    def form_valid(self, form):
        form.save(request=self.request)
        return HttpResponseRedirect(reverse("auth_forgot_password_sent"))

#------------------------------------------------------------
# Edit Password
#------------------------------------------------------------
class UpdatePasswordView(FormView):
    model = User
    form_class = UpdatePasswordForm
    template_name = "accounts/change_password.html"

    def get_success_url(self):
        if self.request.POST.get("next", False):
            return reverse("account_profile_settings")
        else:
            return reverse("account_profile_password")

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)