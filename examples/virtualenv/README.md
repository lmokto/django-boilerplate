Editar los archivos ``postactivate`` y ``postdeactivate`` de entorno virtual.

### postactivate

    vim ~/.virtualenv/myenv/bin/postactivate

    alias root_project="cd ~/project/folder"

    export OLD_PATH=$PATH
    export PATH=~/project/folder/bin:$OLD_PATH

    export OLD_PYTHONPATH=$PYTHONPATH
    export PYTHONPATH=~/projects/folder/src:~/projects/folder/src/app:$OLD_PYTHONPATH

Cambiar ``~/project/folder`` por la ruta del proyecto, tanto en el ``env`` de producción como en el 
de desarrollo. Ahora se tendrá acceso a los archivo ``bin/`` desde cualquier parte.

Con el "comando" ``root_project``, te moverás a la raíz del proyecto equivalente a ``cd /ruta/root/proyecto``

Con ``export PATH=~/project/folder/bin:$OLD_PATH`` se podrá acceder a los archivos de ``shell`` 
desde cualquier parte.

Se añade a ``PYTHONPATH`` los directorios ``~/projects/folder/src`` y ``~/projects/folder/src/app``.

**NOTA:** Los archivos ``settings*.py`` también hace esto ultimo, por lo que no es necesario.

### postdeactivate

    unalias root_project

    export PATH=$OLD_PATH
    export OLD_PATH=""
    export PYTHONPATH=$OLD_PYTHONPATH
    export OLD_PYTHONPATH=""

Cuando se salga del entorno virtual, limpiara las variables puestas cuando se entro.
