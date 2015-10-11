# Descarga paquetes npm y bower, util solo para la inicialización
# del proyecto.
#
# Se ha de tener instalado global gulp y bower.

_script=$(readlink -f $0)
path=$(dirname $(dirname $_script))
path=$path'/src'

cd $path

npm install gulp gulp-concat gulp-uglify gulp-sass --save-dev
bower install --save bootstrap jquery
