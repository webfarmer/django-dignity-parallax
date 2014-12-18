from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from accounts.forms import AuthenticationForm
from django.contrib.auth import views as auth_views
from accounts import views
from django.conf.urls import *

from django.contrib.auth.views import login
from registration.models import RegistrationProfile

urlpatterns = patterns('',
    url(r'^login/$',                            login,  {'authentication_form': AuthenticationForm }, name='auth_login'),
    url(r'^logout/$',                           auth_views.logout, {'template_name': 'registration/logout.html'}, name='auth_logout'),

    url(r'^forgot-password/$' ,                 views.PasswordResetView.as_view(), name='auth_forgot_password'),
    url(r'^forgot-password/sent/$' ,            TemplateView.as_view(template_name="registration/password_reset_done.html"), name='auth_forgot_password_sent'),

    url(r'^accounts/profile/password/$',        login_required(views.UpdatePasswordView.as_view()), name='account_profile_password'),

    ## leave this last
    (r'', include('components.registration.auth_urls')),
)

admin.site.unregister(RegistrationProfile)
