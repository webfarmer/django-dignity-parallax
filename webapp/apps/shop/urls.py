from django.conf.urls import *
from decorators import is_not_main_site
import views

urlpatterns = patterns('shop.views',
    url('^$',                                       is_not_main_site(views.ShopView.as_view()),                 name="shop"),
    url('^checkout/$',                              is_not_main_site(views.CheckoutView.as_view()),             name="checkout"),
)
