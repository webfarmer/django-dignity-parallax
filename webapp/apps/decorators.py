from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def is_main_site(function, alt=False):
    def wrap(request, *args, **kwargs):
        site = Site.objects.get_current()
        if site.domain != "tottagency.com":
            if alt:
                return HttpResponseRedirect(reverse(alt))
            else:
                return HttpResponseRedirect(reverse('shop'))
        else:
            return function(request, *args, **kwargs)

    wrap.__doc__=function.__doc__
    wrap.__name__=function.__name__
    return wrap

def is_not_main_site(function, alt=False):
    def wrap(request, *args, **kwargs):
        site = Site.objects.get_current()
        if site.domain == "tottagency.com":
            if alt:
                return HttpResponseRedirect(reverse(alt))
            else:
                return HttpResponseRedirect(reverse('home'))
        else:
            return function(request, *args, **kwargs)

    wrap.__doc__=function.__doc__
    wrap.__name__=function.__name__
    return wrap