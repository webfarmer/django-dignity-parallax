from django.conf.urls import *
from decorators import is_main_site
import views

urlpatterns = patterns('',
    url('^$',   is_main_site(views.HomeView.as_view()),  name="home"),

    url('^portfolio/(?P<slug>[a-zA-Z0-9_-]+)/$',   is_main_site(views.PortfolioView.as_view()),  name="portfolio"),

   url('^contact/$',   is_main_site(views.ContactView.as_view()),  name="contact"),

   url('^(?P<slug>[a-zA-Z0-9_-]+)/$',   views.PageDetailView.as_view(),  name="page"),

)

