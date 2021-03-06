# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User management
    # url(r'^users/', include("users.urls", namespace="users")),
    # url(r'^accounts/', include('allauth.urls')),

    # Uncomment the next line to enable avatars
    # url(r'^avatar/', include('avatar.urls')),

    # Your stuff: custom urls go here
    url(r'^', include('petition.urls', namespace='petition')),
    url(r'^contact', include('contact.urls', namespace="contact")),
    url(r'^', include('django.contrib.flatpages.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
