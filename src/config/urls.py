from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from apps.home.views import IndexView

urlpatterns = [
    # / (Pagina principal del sitio)
    url(r'^$', IndexView.as_view(), name='index'),

    # /home/*
    url(r'^home/', include('apps.home.urls', namespace='home')),

    # /admin/*
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns.append(
        # /media/:<mixed>path/
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            kwargs={'document_root': settings.MEDIA_ROOT}))
