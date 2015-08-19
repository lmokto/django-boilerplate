http://www.snicoper.com

Pequeña plantilla para proyectos Django.

Por defecto usa Bootstrap como framework css.

### Instalacion

    django-admin.py startproject --template=https://github.com/snicoper/dj-estructura/archive/master.zip nombre_proyecto

    cd nombre_proyecto/src/

    bower install
    npm install

### Migracion y super usuario

    ./manage.py migrate
    ./manage.py createsuperuser

### manage_prod.py y manage_test.py

Usar en desarrollo ``manage.py`` para produccion ``prod_manage.py`` y para tests ``test_manage.py``
