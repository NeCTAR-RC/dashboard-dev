FROM ubuntu:18.04

RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-venv python3-dev libpython3.6 git build-essential mariadb-client
RUN python3 -m venv /venv

ENV DJANGO_SETTINGS_MODULE=openstack_dashboard.settings
ENV PATH=/venv/bin:$PATH

RUN python -m pip install -U pip setuptools wheel
RUN python -m pip install pyyaml pbr

WORKDIR /config
COPY repos.yaml pip_helper.py constraints.txt uwsgi.ini /config/

COPY entrypoint.sh setup.sh /
RUN chmod u+x /entrypoint.sh /setup.sh

WORKDIR /src
ENTRYPOINT ["/entrypoint.sh"]
