from django.conf.urls import url

from . import views

urlpatterns = [

    # /home/
    url(
        regex='^$',
        view=views.IndexView.as_view(),
        name='index'
    ),
]
