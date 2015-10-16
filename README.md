http://www.snicoper.com

Pequeña plantilla para proyectos Django.

Por defecto usa Bootstrap como framework css.

### Instalación

    django-admin.py startproject --template=https://github.com/snicoper/dj-estructura/archive/master.zip nombre_proyecto

    cd nombre_proyecto/

    chmod +x bin/permissions.sh
    ./bin/permissions.sh

    # Esto instalara paquetes de bower y npm editar archivo ./bin/init_npm.sh con los paquetes que se quiera instalar.
    ./bin/init_npm.sh

### Migracion y super usuario (desarrollo)

    ./manage.py migrate
    ./manage.py createsuperuser

### manage_prod.py y manage_test.py

Usar en desarrollo ``manage.py`` para producción ``prod_manage.py`` y para tests ``test_manage.py``
