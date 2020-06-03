# Dashboard Dev Environment

This project uses Docker Compose to create a development environment
for the OpenStack dashboard and its plugins.


## Configuration

### Repo file

`dashboard/repos.yaml`

This configures which source repositories are cloned and installed
into the dashboard virtualenv. The `pip_helper.py` script clones
any repos that don't already exist in the /src directory. If a directory
already exists in /src, it just does the equivalent of `pip install -e ./dir`
instead. This ensures that your local changes are not blown away.

### Settings files

`settings.py`

This file contains generic settings.

`environment_settings.py`

This file containers any environment-specific settings that
will override anything in the `settings.py` file. It is assumed
that this file is managed outside of this repository.


### Environment variables

`DB_SERVERS`

This is used specify the backends used by the HAProxy service.
It should be a comma-separated list of IPs or hostnames.


## Run

To create the stack, start docker-sync first and then run docker-compose:

    $ docker-sync start
    $ docker-compose up --build
    $ open http://localhost:8000

On subsequent runs you can omit the --build argument.

Alternatively, you can run docker-compose daemonized and
just watch the logs of a specific container:

    $ docker-compose up -d
    $ docker-compose logs -f logs


## Stop

To stop all the containers:

    $ docker-compose down
    $ docker-sync stop


## Destroy

To destroy all of the data volumes:

    $ docker-compose down -v
    $ docker-sync clean

Your local src/ directory will not be deleted during this process.
If you want a completely clean slate just delete its contents manually.

## Containers

`memcached`

Used by the dashboard for user sessions and caching.

`db`

This is actually a HAProxy service that proxies to
the actual DB backends. In Core Services this is usually
a MariaDB cluster in our dev cloud.

`dashboard`

This is the container with the actual dashboard code. It runs
uWSGI on a TCP socket to serve the app. When the container starts
up it checks the contents of /src (synced from your host) and clones
source repositories as needed. uWSGI is set up to do auto-reloading
when any python source code is changed in /src.

`nginx`

Serves the app from the uWSGI socket and also the static content from the
volume it shares with the `dashboard` container. The dashboard service is
exposed from this container on host port 8080.

`logs`

This is just a sidecar that tails the dashboard's debug log file to stdout
so it appears in the docker-compose logs.


## Running with a local DB

By default the docker-compose stack points to an existing database server
setup. It's also possible to run your own DB locally as part of the stack
by including an extra compose file:

    export COMPOSE_FILE=docker-compose.yml:docker-compose-local-db.yml
    docker-compose up

This will create a single MariaDB instance and an empty `dashboard` database.
When the dashboard container starts it will run `django-admin migrate` to
propagate the tables.

## Debugging

PDB debugging is supported by attaching to the dashboard container with Docker:

    docker attach dashboard-dev_dashboard_1


## More about docker-sync

Host-to-container mounts in Docker on Mac OS come with a huge
performance penalty to the point of being practically unusable.
To get around this we use the docker-sync project to get native
performance inside the container but still support two-way sync
between host and container.

docker-sync creates an "external" volume that is consumed by the
docker-compose stack. A sync container created by docker-sync then
that mounts that same volume and handles the sync between the host
machine and the volume.

docker-sync requires Ruby and the docker-sync gem.

    $ gem install docker-sync
    $ docker-sync start
    ...
     success  Sync container started
     success  Starting Docker-Sync in the background

You can use the `stop` and `clean` commands to stop the daemon
and delete the volume.
