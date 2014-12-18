from django.conf.urls import *
from decorators import is_main_site
import views

urlpatterns = patterns('',
    url('^$',   is_main_site(views.HomeView.as_view()),  name="home"),
)
