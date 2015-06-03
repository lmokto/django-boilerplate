#!/bin/bash

NAME="snicoper.com" # Name of the application
DJANGODIR=/home/snicoper/www/snicoper.com/src/ # Django project directory
LOGFILE=/home/snicoper/www/snicoper.com/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
USER=snicoper # the user to run as
GROUP=snicoper # the group to run as
ADDRESS=127.0.0.1:8001
NUM_WORKERS=3 # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=base.settings.prod # which settings file should Django use
DJANGO_WSGI_MODULE=base.wsgi # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /home/snicoper/.virtualenvs/snicoper.com/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
    --workers $NUM_WORKERS \
    --bind=$ADDRESS \
    --user=$USER --group=$GROUP \
    --log-level=debug \
    --log-file=$LOGFILE 2>>$LOGFILE
