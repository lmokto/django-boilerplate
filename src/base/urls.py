from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',

    # /*
    url(
        regex=r'^$',
        view=include('apps.home.urls')),

    # /home/*
    url(
        regex=r'^home/',
        view=include('apps.home.urls')),

    # /admin/*
    url(
        regex=r'^admin/',
        view=include(admin.site.urls)),
)
