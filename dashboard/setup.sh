#!/bin/bash -ex

python /config/pip_helper.py /config/repos.yaml /src /config/constraints.txt
python -m pip install uwsgi python-memcached ${PIP_EXTRA_DEPENDENCIES}

DASHBOARD_DIR="/src/horizon/openstack_dashboard"
ENABLED_DIR="$DASHBOARD_DIR/local/enabled"
SETTINGS_FILE="$DASHBOARD_DIR/local/local_settings.py"
SETTINGS_DIR="$DASHBOARD_DIR/local/local_settings.d"

ln -sf /config/local_settings.py "$SETTINGS_FILE"
ln -sf /config/environment_settings.py "$SETTINGS_DIR/environment_settings.py"

cp -a /src/nectar-dashboard/nectar_dashboard/enabled/_[0-9]* $ENABLED_DIR/
cp -a /src/heat-dashboard/heat_dashboard/enabled/_1*.py $ENABLED_DIR/
cp -a /src/manila-ui/manila_ui/local/enabled/_{8,9}*.py $ENABLED_DIR/
cp -a /src/octavia-dashboard/octavia_dashboard/enabled/_1*.py $ENABLED_DIR/
cp -a /src/murano-dashboard/muranodashboard/local/enabled/_*.py $ENABLED_DIR/
cp -a /src/trove-dashboard/trove_dashboard/enabled/_1*.py $ENABLED_DIR/

django-admin collectstatic --noinput
django-admin compress --force
