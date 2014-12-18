from django.views.generic import TemplateView

class ShopView(TemplateView):
    template_name = "shop/home.html"

class CheckoutView(TemplateView):
    template_name = "shop/checkout.html"