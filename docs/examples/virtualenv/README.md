Editar los archivos ``postactivate`` y ``postdeactivate`` de entorno virtual.

### postactivate

    vim ~/.virtualenv/myenv/bin/postactivate

    alias root_project="cd ~/project/folder"

    export OLD_PATH=$PATH
    export PATH=~/project/folder/bin:$OLD_PATH

    export OLD_PYTHONPATH=$PYTHONPATH
    export PYTHONPATH=~/project/folder/src:$OLD_PYTHONPATH

Cambiar ``~/project/folder`` por la ruta del proyecto, tanto en el ``env`` de producción como en el de desarrollo. Ahora se tendrá acceso a los archivo ``bin/`` desde cualquier parte.

### postdeactivate

    unalias root_project

    export PATH=$OLD_PATH
    export OLD_PATH=""
    export PYTHONPATH=$OLD_PYTHONPATH
    export OLD_PYTHONPATH=""
