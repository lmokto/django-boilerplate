# NOTA: Usar ./manage makemigrations nombre_app y
#   ./manage migrate --fake

_script=$(readlink -f $0)
path=$(dirname $(dirname $_script))
path=$path'/src'

find $path -name "migrations" -exec rm -rf {} \;

echo 'Eliminados los directorios migrations'

echo 'Usar ./manage makemigrations nombre_app'
echo 'y ./manage migrate --fake'
