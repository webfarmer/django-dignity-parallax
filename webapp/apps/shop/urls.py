from django.conf.urls import *
import views

urlpatterns = patterns('shop.views',
    url('^$',                                       views.ShopView.as_view(),                 name="shop"),
    url('^checkout/$',                              views.CheckoutView.as_view(),             name="checkout"),
)
