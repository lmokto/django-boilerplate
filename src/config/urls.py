from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve

urlpatterns = [
    # / (Pagina principal del sitio)
    url(r'^$', include('apps.home.urls', namespace='home')),

    # /home/*
    url(r'^home/', include('apps.home.urls', namespace='home')),

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
