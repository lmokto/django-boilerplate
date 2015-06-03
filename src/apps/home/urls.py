from django.conf.urls import url

from . import views

urlpatterns = [
    
    # /home/ or / # Dependiendo de base.urls.py
    url(
        regex=r'^$',
        view=views.IndexView.as_view(),
        name='home.index'),
]
