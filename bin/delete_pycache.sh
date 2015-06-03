_script=$(readlink -f $0)
path=$(dirname $(dirname $_script))
path=$path'/src'

find $path -name "__pycache__" -exec rm -rf {} \;

echo 'Eliminados los directorios __pycache__'
