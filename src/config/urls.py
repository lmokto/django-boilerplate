from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve

from home.views import IndexView

urlpatterns = [
    ##################################################
    # / Pagina de inicio.
    url(r'^$', IndexView.as_view(), name='home_page'),
    ##################################################

    # /home/*
    url(r'^home/', include('home.urls')),

    # /admin/*
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns.append(
        # /media/:<mixed>path/
        url(
            r'^media/(?P<path>.*)$',
            serve,
            kwargs={'document_root': settings.MEDIA_ROOT}
        )
    )
