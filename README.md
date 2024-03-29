http://www.snicoper.com

Estructura que utilizo para crear practicas con Django con una base ya echa.

Para cambiar/añadir paquetes con ``pip`` ver ``./requeriments/*.txt``.

# Instalación

Crear un entorno virtual con ``virtualenv`` o ``virtualenvwrapper`` y crear el proyecto.

    django-admin.py startproject --template=https://github.com/snicoper/django-boilerplate/archive/master.zip nombre_proyecto
    cd nombre_proyecto/

    pip install -r requirements/(local|prod|tests).txt

Dar permisos a los archivos, esto pondrá los directorios con permisos ``775 drwxrwxr-x.`` y los archivos ``664 -rw-rw-r--.``, si se quiere cambiar, editar el archivo ``./bin/permissions``.

A parte dará permisos de ejecución a algunos archivos, los archivos ``./bin/*`` y ``./manage*.py``.

    chmod +x bin/permissions.sh
    ./bin/permissions.sh

## Migración y super usuario (desarrollo)

    ./manage.py migrate
    ./manage.py createsuperuser

## manage_prod.py y manage_test.py

Para no tener que estar cambiando con ``./manage.py command --settings=archivo.settings``, hay 3 archivos ``manage``, cada uno de ellos apunta al archivo ``settings`` que corresponde.

* ``manage.py``: Para desarrollo.
* ``manage_prod.py``: Para producción.
* ``manage_test.py``: Para tests.

## Node

Editar ``./.package.json`` para los paquetes de **nodejs**

    npm install

Para actualizar los paquetes, usar [npm-check-updates](https://www.npmjs.com/package/npm-check-updates)

    sudo npm install -g npm-check-updates

    # Mostrar paquetes con actualizaciones.
    ncu

    # Actualizarlos
    ncu -u

### Scripts en package.json

- ``npm run gulp``: Lo mismo que ``gulp``
- ``npm run sphinx``: Lo mismo que ``gulp sphinx``

## Bower

Actualmente instala

- [JQuery](https://jquery.com/)
- [font-awesome](https://fortawesome.github.io/Font-Awesome/)
- [Materializecss](http://materializecss.com)

Instalar bower a nivel global

    sudo npm install bower -g

Los paquetes los instala en ``./src/static/vendor/``

    bower install

Para actualizar los paquetes, usar [npm-check-updates](https://www.npmjs.com/package/npm-check-updates)

    npm install -g npm-check-updates

    ncu -m bower

### gulpfile.js

- ``gulp``: Unifica y minifica los archivos ``.js`` y ``.scss``
- ``gulp style:sass``: Unifica y minifica los archivos ``.scss``
- ``gulp scripts:js``: Unifica y minifica los archivos ``.js``
- ``gulp watch``: Escucha los directorios ``.js`` y ``.scss``.
- ``gulp build-docs``: Re construye los docs Sphinx (``make html``)
- ``gulp sphinx``: Escucha si hay un cambio en ``./docs``.

## Reinstalar en desarrollo.

Para una reinstalación rapida en la etapa de desarrollo.

Editar las variables del archivo ``bin/reinstall_dev``.

- ``VIRTUAL_ENV_NAME``: Nombre del virtualenv (virtualenvwrapper)
- ``USER_USERNAME``: Nombre del super usuario en django
- ``USER_PASSWORD``: Contraseña del super usuario en django
- ``USER_EMAIL``: Email del super usuario en django
- ``DATABASE_NAME``: Nombre de la base de datos
- ``DATABASE_USER``: Usuario de la base de datos
- ``SITE_DOMAIN``: ``domain`` del Framework Site
- ``SITE_NAME``: ``name`` del Framework Site

Ejecutar ``./bin/reinstall_dev``
