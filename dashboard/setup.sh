#!/bin/bash -ex

python /config/pip_helper.py /config/repos.yaml /src /src/nectar-dashboard/upper-constraints.txt

python -m pip install uwsgi python-memcached ${PIP_EXTRA_DEPENDENCIES}

DASHBOARD_DIR="/src/horizon/openstack_dashboard"
ENABLED_DIR="$DASHBOARD_DIR/local/enabled"
SETTINGS_FILE="$DASHBOARD_DIR/local/local_settings.py"
SETTINGS_DIR="$DASHBOARD_DIR/local/local_settings.d"

ln -sfv /config/local_settings.py "$SETTINGS_FILE"
ln -sfv /config/environment_settings.py "$SETTINGS_DIR/environment_settings.py"

rm -rf ${ENABLED_DIR}/*
touch ${ENABLED_DIR}/__init__.py

cp -a /src/nectar-dashboard/nectar_dashboard/enabled/_[0-9]* $ENABLED_DIR/
cp -a /src/nectar-dashboard/nectar_dashboard/enabled/usage/_[0-9]* $ENABLED_DIR/
# cp -a /src/heat-dashboard/heat_dashboard/enabled/_1*.py $ENABLED_DIR/
cp -a /src/manila-ui/manila_ui/local/enabled/_{8,9}*.py $ENABLED_DIR/
cp -a /src/magnum-ui/magnum_ui/enabled/_1*.py $ENABLED_DIR/
cp -a /src/octavia-dashboard/octavia_dashboard/enabled/_1*.py $ENABLED_DIR/
cp -a /src/murano-dashboard/muranodashboard/local/enabled/_*.py $ENABLED_DIR/
cp -a /src/trove-dashboard/trove_dashboard/enabled/_1*.py $ENABLED_DIR/
cp -a /src/warre-dashboard/warre_dashboard/enabled/_1*.py $ENABLED_DIR/
cp -a /src/designate-dashboard/designatedashboard/enabled/_1*.py $ENABLED_DIR/

cp -a /src/nectar-dashboard/nectar_dashboard/local_settings.d/_50_nectar.py $SETTINGS_DIR/
cp -a /src/murano-dashboard/muranodashboard/local/local_settings.d/_50_murano.py $SETTINGS_DIR/

DEFAULT_POLICIES_DIR=/src/nectar-dashboard/policy/default_policies
mkdir -p $DEFAULT_POLICIES_DIR
cp -r /src/horizon/openstack_dashboard/conf/default_policies/* $DEFAULT_POLICIES_DIR/
cp -a /src/manila-ui/manila_ui/conf/default_policies/manila.yaml $DEFAULT_POLICIES_DIR/
# cp -a /src/heat-dashboard/heat_dashboard/conf/default_policies/heat.yaml $DEFAULT_POLICIES_DIR/

if [ -n "$DJANGO_MIGRATE" ]; then
   django-admin migrate
fi
django-admin collectstatic --noinput
django-admin compress --force
