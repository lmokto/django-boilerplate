from django.contrib.sites.models import Site


def site_processor(request):
    """Obtener nombre de dominio y nombre a mostrar del Site actual."""
    return {'site': Site.objects.get_current()}
