from django.conf import settings
from mails.email import myMailer
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.models import User

from django.utils.safestring import mark_safe
from django import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm as AuthAuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import UNUSABLE_PASSWORD_PREFIX
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.urlresolvers import reverse

#------------------------------------------------------------
# Login
#------------------------------------------------------------
class AuthenticationForm(AuthAuthenticationForm):
    error_messages = {
        'invalid_login': _("Please enter a correct username and password. "
                           "Note that both fields are case-sensitive."),
        'no_cookies': _("Your Web browser doesn't appear to have cookies "
                        "enabled. Cookies are required for logging in."),
        'inactive': _("Please activate your account."),
        }

    username = forms.EmailField(label=_("E-mail"), widget=forms.TextInput(attrs={"maxlength":75,"class":"input-large search-query"}))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={"class":"input-large search-query"}))


#------------------------------------------------------------
# Edit Password
#------------------------------------------------------------
class UpdatePasswordForm(forms.Form):
    old_password = forms.CharField(label=_("Old password"), widget=forms.PasswordInput, required=False)
    new_password = forms.CharField(label=_("New password"), widget=forms.PasswordInput, required=False)
    confirm_password = forms.CharField(label=_("Confirm password"), widget=forms.PasswordInput, required=False)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(UpdatePasswordForm, self).__init__(*args, **kwargs)

    def save(self):
        if self.cleaned_data["old_password"] != "" and self.cleaned_data["new_password"] != "" and self.cleaned_data["confirm_password"] != "":
            self.request.user.set_password(self.cleaned_data["new_password"])
            self.request.user.save()

            activate_link = settings.SITE_DOMAIN
            link = '<a href="%s%s">%s</a>' % (activate_link, reverse("auth_login"), _('Click here').title())
            link_password = '<a href="%s%s">%s</a>' % (activate_link, reverse("auth_forgot_password"),_('Click Here').title())
            link_contact = '<a href="%s%s">%s</a>' % (activate_link, reverse("contact"),_('Contact us').title())

            mail = myMailer(
                to = self.request.user.email,
                slug = "update-password",
                user=self.request.user,
                site_url=settings.SITE_DOMAIN,
                link = mark_safe(link),
                link_contact = mark_safe(link_contact),
                link_password = mark_safe(link_password)
            ); mail.send()

            messages.success(self.request, 'Your password was successfully saved.')

    def clean(self):
        if self.cleaned_data["old_password"] != "" and self.cleaned_data["new_password"] != "" and self.cleaned_data["confirm_password"] != "":
            if self.request.user.check_password(self.cleaned_data["old_password"]):
                if self.cleaned_data["new_password"] != self.cleaned_data["confirm_password"]:
                    self._errors["new_password"] = "incorrect"; self._errors["confirm_password"] = "incorrect"
                    messages.error(self.request, "Your new password and confirmed password did not match.")
                    raise forms.ValidationError("Your new password and confirmed password did not match.")
            else:
                self._errors["old_password"] = "incorrect"
                messages.error(self.request, "Your old password was incorrect.")
                raise forms.ValidationError("Your old password was incorrect.")
        else:
            if self.cleaned_data["old_password"] == "" and self.cleaned_data["new_password"] == "" and self.cleaned_data["confirm_password"] == "":
                messages.success(self.request, 'Your password was not changed.')
            else:
                self._errors["old_password"] = "incorrect"; self._errors["new_password"] = "incorrect"; self._errors["confirm_password"] = "incorrect"
                messages.error(self.request, "One of the fields was blank. Please try again.")
                raise forms.ValidationError("blank field.")
        return self.cleaned_data



class PasswordResetForm(forms.Form):
    error_messages = {
        'unknown': _("That e-mail address doesn't have an associated "
                     "user account. Are you sure you've registered?"),
        'unusable': _("The user account associated with this e-mail "
                      "address cannot reset the password."),
        }
    email = forms.EmailField(label=_("E-mail"), max_length=150)

    def clean_email(self):
        """ Validates that an active user exists with the given email address. """
        email = self.cleaned_data["email"]
        self.users_cache = User.objects.filter(email__iexact=email, is_active=True)
        if not len(self.users_cache):
            raise forms.ValidationError(self.error_messages['unknown'])
        if any((user.password == UNUSABLE_PASSWORD_PREFIX)
            for user in self.users_cache):
            raise forms.ValidationError(self.error_messages['unusable'])

        self.user = self.users_cache[0]
        return email

    def save(self, request):
        user = self.user

        site_url = settings.SITE_DOMAIN
        token_generator = PasswordResetTokenGenerator()

        link = '<a href="%s%s">%s</a>' % ( site_url, reverse('auth_password_reset_confirm',
                                               args=(),
                                               kwargs={ 'uidb64':  urlsafe_base64_encode(str(user.id)),
                                                       'token':    token_generator.make_token(user)
                                               }), _('Click Here To Reset').title())

        mail = myMailer(slug = "forgot-password",
            to = user.email,
            user = user,
            link = mark_safe(link),
            site_url = mark_safe(site_url),
        ) ; mail.send()
