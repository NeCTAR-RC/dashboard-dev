FROM ubuntu:20.04

RUN apt-get update && apt-get install -y --no-install-recommends python3.8 python3-venv python3.8-dev libpython3.8 libffi-dev libmysqlclient-dev git build-essential mariadb-client
RUN python3.8 -m venv /venv

ENV DJANGO_SETTINGS_MODULE=openstack_dashboard.settings
ENV PATH=/venv/bin:$PATH

RUN python3.8 -m pip install -U pip setuptools wheel
RUN python3.8 -m pip install pyyaml pbr mysqlclient

WORKDIR /config
COPY repos.yaml pip_helper.py constraints.txt uwsgi.ini /config/

COPY entrypoint.sh setup.sh /
RUN chmod u+x /entrypoint.sh /setup.sh

WORKDIR /src
ENTRYPOINT ["/entrypoint.sh"]
