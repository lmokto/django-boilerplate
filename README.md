http://www.snicoper.com

Estructura que utilizo para crear practicas con Django con una base ya echa.

Para cambiar/añadir paquetes con ``pip`` ver ``./requeriments/*.txt``.

### Instalación

Crear un entorno virtual en Python con ``pip`` y crear el proyecto.

    django-admin.py startproject --template=https://github.com/snicoper/dj-estructura/archive/master.zip nombre_proyecto
    cd nombre_proyecto/

Dar permisos a los archivos, esto nos pondrá las carpeta con permisos ``775 drwxrwxr-x.`` y los archivos ``664 -rw-rw-r--.``, si se quiere cambiar, editar el archivo ``./bin/permissions.sh``.

A parte dará permisos de ejecución a algunos archivos, a los archivos ``./bin/*`` y ``./src/manage.py`` entre otros.

    chmod +x bin/permissions.sh
    ./bin/permissions.sh

### Migracion y super usuario (desarrollo)

    ./manage.py migrate
    ./manage.py createsuperuser

### manage_prod.py y manage_test.py

Para no tener que estar cambiando con ``./manage.py comando --settings=archivo.settings``, hay 3 archivos ``manage``, cada uno de ellos apunta al archivo ``settings`` que corresponde.

* ``manage.py``: Para desarrollo.
* ``manage_prod.py``: Para producción.
* ``manage_test.py``: Para tests.
