from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, DetailView, FormView
from models import Page, ParallaxConfig, Team, Testimonial, Portfolio, Contact
from parallax.forms import ContactForm


class HomeView(TemplateView):
    template_name = "parallax/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        config = ParallaxConfig.objects.get(id=1)
        context["config"] = config

        context["team_list"] = Team.objects.all().order_by("order")
        context["testimonial_list"] = Testimonial.objects.all().order_by("order")
        context["portfolio_list"] = Portfolio.objects.all().order_by("order")

        context["header_nav"] = "parallax/partials/headers/%s_nav.html" % config.parallax_id
        context["header"] = "parallax/partials/headers/%s.html" % config.parallax_id
        context["javascript"] = "parallax/partials/headers/%s_js.html" % config.parallax_id
        return context


class PortfolioView(DetailView):
    model = Portfolio
    template_name = "parallax/portfolio.html"
    context_object_name = "portfolio"

    def get_context_data(self, **kwargs):
        context = super(PortfolioView, self).get_context_data(**kwargs)
        config = ParallaxConfig.objects.get(id=1)
        context["config"] = config

        context["header_nav"] = "parallax/partials/headers/%s_nav.html" % config.parallax_id
        context["header"] = "parallax/partials/headers/07.html"
        context["javascript"] = "parallax/partials/headers/07_js.html"
        return context


class PageDetailView(DetailView):
    model = Page
    template_name = "parallax/page.html"
    context_object_name = "page"

    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)

        config = ParallaxConfig.objects.get(id=1)
        context["config"] = config

        context["header_nav"] = "parallax/partials/headers/%s_nav.html" % config.parallax_id
        context["header"] = "parallax/partials/headers/07.html"
        context["javascript"] = "parallax/partials/headers/07_js.html"
        return context


class ContactView(FormView):
    model = Contact
    template_name = 'parallax/contact.html'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)

        config = ParallaxConfig.objects.get(id=1)
        context["config"] = config

        context["header_nav"] = "parallax/partials/headers/%s_nav.html" % config.parallax_id
        context["header"] = "parallax/partials/headers/07.html"
        context["javascript"] = "parallax/partials/headers/07_js.html"

        try:
            context["page"] = Page.objects.get(slug="contact")
        except:
            pass
        return context

    def get_success_url(self):
        messages.success(self.request,"Your mail was successfully sent!")
        return reverse("contact")

    def form_valid(self, form):
        print form
        form.save(self.request)
        return super(ContactView, self).form_valid(form)