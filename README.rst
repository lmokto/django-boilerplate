<http://www.snicoper.com>_

Modificar las configuraciones de la base de datos en los archivos de ``src/base/settings/(prod|local|test)``.

En producción, modificar ``src/base/settings/prod.py`` la variable ``ALLOWED_HOSTS``.

**Importante!** Poner en ``src/base/settings/prod.py`` la variable ``SECRET_KEY``, generar
un nuevo proyecto y copiarla o desde
`Django Secret Key Generator <http://www.miniwebtool.com/django-secret-key-generator/>`_ generar
una nueva.

Sincronizar la base de datos y crear un super usuario.

.. code-block:: bash

    cd src
    ./(|prod_)manage.py migrate
    ./(|prod_)manage.py createsuperuser

Para test

.. code-block:: bash

    cd src
    ./test_manage.py test
