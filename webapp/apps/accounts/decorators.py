from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def is_logged_in(function, alt=False):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated():
            if not alt:
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponseRedirect(reverse(alt))
        else:
            return function(request, *args, **kwargs)

    wrap.__doc__=function.__doc__
    wrap.__name__=function.__name__
    return wrap

def is_not_logged_in(function, alt=False):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated():
            if not alt:
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponseRedirect(reverse(alt))
        else:
            return function(request, *args, **kwargs)

    wrap.__doc__=function.__doc__
    wrap.__name__=function.__name__
    return wrap