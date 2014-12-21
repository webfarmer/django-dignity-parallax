from django.conf.urls import *
import views

urlpatterns = patterns('',
    url('^$',   views.HomeView.as_view(),  name="home"),

    url('^portfolio/(?P<slug>[a-zA-Z0-9_-]+)/$',   views.PortfolioView.as_view(),  name="portfolio"),

   url('^contact/$',   views.ContactView.as_view(),  name="contact"),

   url('^(?P<slug>[a-zA-Z0-9_-]+)/$',   views.PageDetailView.as_view(),  name="page"),

)

