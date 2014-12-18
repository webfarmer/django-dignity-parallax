from django.conf.urls import *
import views

urlpatterns = patterns('',
    url('^$',   views.HomeView.as_view(),  name="home"),
)
