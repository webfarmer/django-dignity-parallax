from django.conf.urls import *
from django.contrib.auth.decorators import login_required
from decorators import is_not_main_site
import views

urlpatterns = patterns('shop.views',
    url('^$',                                       is_not_main_site(login_required(views.ShopView.as_view())),                 name="shop"),
    url('^checkout/$',                              is_not_main_site(login_required(views.CheckoutView.as_view())),             name="checkout"),
)
