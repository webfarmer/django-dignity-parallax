from django.conf import settings

def pages(request):

    context={}
    context["slug"] = request.path
    context["PROJECT_NAME"] = settings.PROJECT_NAME
    context["PROJECT_DOMAIN"] = settings.PROJECT_DOMAIN
    context["page_slug"] = request.get_full_path()

    return context