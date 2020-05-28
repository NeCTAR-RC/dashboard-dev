#!/bin/bash -ex

if [ -z "$SKIP_SETUP" ]; then
    /setup.sh
fi

exec uwsgi --ini /config/uwsgi.ini
