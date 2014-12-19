from django.views.generic import TemplateView, DetailView
from models import Page, ParallaxConfig


class HomeView(TemplateView):
    template_name = "parallax/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        config = ParallaxConfig.objects.get(id=1)
        context["config"] = config
        context["header_nav"] = "parallax/partials/headers/%s_nav.html" % config.parallax_id
        context["header"] = "parallax/partials/headers/%s.html" % config.parallax_id
        context["javascript"] = "parallax/partials/headers/%s_js.html" % config.parallax_id
        return context


class PageDetailView(DetailView):
    model = Page
    template_name = "parallax/page.html"
    context_object_name = "page"
