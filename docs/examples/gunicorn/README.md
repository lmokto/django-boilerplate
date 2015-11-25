    sudo cp gunicorn.service /etc/systemd/system/gunicorn.service

    sudo systemctl start gunicorn.service
    sudo systemctl enable gunicorn.service

Cambiar usuario y grupo
