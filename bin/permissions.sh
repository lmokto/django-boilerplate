#!/bin/bash

# Cambia/se asegura, de los permisos en el sitio,
# Todos los archivos con permisos 644 y todos los
# directorios 755.
# Algunos archivos necesitan permisos de ejecucion.

# drwxrwxr-x
folders=775

# -rw-rw-r--
files=664
_script=$(readlink -f $0)
path=$(dirname $(dirname $_script))

echo "Cambiando permisos de directorios $folders"
find $path -type d -exec chmod $folders {} \;
echo "Cambiando permisos de archivos $files"
find $path -type f -exec chmod $files {} \;

########################
# Permisos de ejecucion.
########################

echo "Cambiando permisos de ejecucion a $path/bin/permissions.sh"
chmod +x "$path/bin/permissions.sh"

echo "Cambiando permisos de ejecucion a $path/bin/gunicorn_start.sh"
chmod +x "$path/bin/gunicorn_start.sh"

echo "Cambiando permisos de ejecucion a $path/bin/delete_pycache.sh"
chmod +x "$path/bin/delete_pycache.sh"

echo "Cambiando permisos de ejecucion a $path/bin/delete_migrations.sh"
chmod +x "$path/bin/delete_migrations.sh"

echo "Cambiando permisos de ejecucion a $path/src/manage.py"
chmod +x "$path/src/manage.py"

echo "Cambiando permisos de ejecucion a $path/src/prod_manage.py"
chmod +x "$path/src/prod_manage.py"

echo "Cambiando permisos de ejecucion a $path/src/test_manage.py"
chmod +x "$path/src/test_manage.py"

echo "Cambiando permisos de ejecucion a $path/bin/init_npm.sh"
chmod +x "$path/bin/init_npm.sh"

echo "Terminado el cambio de permisos."
