import os
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/filebrowser/',              include('filebrowser.urls')),
    url(r'^media/tinymce/',                  include('tinymce.urls')),
    url(r'^admin/',                          include(admin.site.urls)),

    url(r'^',                                include('parallax.urls')),
    url(r'^',                                include('accounts.urls')),
    url(r'^shop/',                           include('shop.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(.*)$',                  'django.views.static.serve', {'document_root': settings.PROJECT_DIR + '/static/' }),
        (r'^media/(.*)$',                   'django.views.static.serve', {'document_root': settings.PROJECT_DIR + '/media/' }),
        (r'^robots.txt$',                   'django.views.static.serve', { 'path' : "/static/robots.txt", 'document_root': settings.PROJECT_ROOT, 'show_indexes': False } ),
        (r'^favicon.ico/$',                 'django.views.static.serve', { 'path' : "/static/favicon.ico", 'document_root': settings.PROJECT_ROOT, 'show_indexes': False } ),
    )