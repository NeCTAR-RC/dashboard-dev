FROM ubuntu:22.04

RUN apt-get update && apt-get install -y --no-install-recommends python3.10 python3-venv python3.10-dev libpython3.10 libffi-dev libmysqlclient-dev git build-essential pkg-config mariadb-client
RUN python3.10 -m venv /venv

ENV DJANGO_SETTINGS_MODULE=openstack_dashboard.settings
ENV PATH=/venv/bin:$PATH

RUN python3.10 -m pip install -U pip setuptools wheel
RUN python3.10 -m pip install pyyaml pbr mysqlclient

WORKDIR /config
COPY repos.yaml pip_helper.py uwsgi.ini /config/

COPY entrypoint.sh setup.sh /
RUN chmod u+x /entrypoint.sh /setup.sh

WORKDIR /src
ENTRYPOINT ["/entrypoint.sh"]
