from django.views.generic import TemplateView, DetailView
from models import Page


class HomeView(TemplateView):
    template_name = "parallax/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        return context


class PageDetailView(DetailView):
    template_name = "parallax/page.html"
    model = Page
    context_object_name = "page"
