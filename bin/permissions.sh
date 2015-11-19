#!/usr/bin/env bash

# Cambia/se asegura, de los permisos en el sitio,
# Todos los archivos con permisos 644 y todos los
# directorios 755.
# Algunos archivos necesitan permisos de ejecución.

source variables

# drwxrwxr-x
folders=775

# -rw-rw-r--
files=664

# Por defecto excluye directorios libs(bower) y node_modules(node)
echo "Cambiando permisos de directorios $folders"
find $PROJECT_ROOT -type d ! -path "libs" ! -path "node_modules" -exec chmod $folders {} \;
echo "Cambiando permisos de archivos $files"
find $PROJECT_ROOT -type f ! -path "libs" ! -path "node_modules" -exec chmod $files {} \;

########################
# Permisos de ejecución.
########################

echo "Cambiando permisos de ejecución a $BIN_ROOT/permissions"
chmod +x "$BIN_ROOT/permissions"

echo "Cambiando permisos de ejecución a $BIN_ROOT/gunicorn_start"
chmod +x "$BIN_ROOT/gunicorn_start"

echo "Cambiando permisos de ejecución a $BIN_ROOT/delete_pycache"
chmod +x "$BIN_ROOT/delete_pycache"

echo "Cambiando permisos de ejecución a $BIN_ROOT/delete_migrations"
chmod +x "$BIN_ROOT/delete_migrations"

echo "Cambiando permisos de ejecución a $BIN_ROOT/npm_install"
chmod +x "$BIN_ROOT/npm_install"

echo "Cambiando permisos de ejecución a $SRC_ROOT/manage.py"
chmod +x "$SRC_ROOT/manage.py"

echo "Cambiando permisos de ejecución a $SRC_ROOT/prod_manage.py"
chmod +x "$SRC_ROOT/prod_manage.py"

echo "Cambiando permisos de ejecución a $SRC_ROOT/test_manage.py"
chmod +x "$SRC_ROOT/test_manage.py"

echo "Terminado el cambio de permisos."

