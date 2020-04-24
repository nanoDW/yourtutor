#!/bin/sh

if [ "$1" = 'server' ]; then
    export FLASK_ENV=production
    export FLASK_APP=backend.app:create_app
    backend db upgrade
    backend init
    gunicorn -w 2 -b 0.0.0.0:5000 backend.wsgi:app --preload
fi
