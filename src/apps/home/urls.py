from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',

    # /home/ or / # Dependiendo de base.urls.py
    url(
        regex=r'^$',
        view=views.IndexView.as_view(),
        name='home.index'),
)
