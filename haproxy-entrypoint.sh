#!/bin/bash

HAPROXY_CONF="/usr/local/etc/haproxy/haproxy.cfg"

cat > $HAPROXY_CONF <<EOF
global
  log  127.0.0.1 local0
  log  127.0.0.1 local1 notice
  maxconn  4096

defaults
  log  global
  maxconn  8000
  option  redispatch
  retries  3
  stats  enable
  timeout  http-request 10s
  timeout  queue 1m
  timeout  connect 10s
  timeout  client 1m
  timeout  server 1m
  timeout  check 10s

listen db
  bind *:3306
  mode tcp
  balance source
  log 127.0.0.1 local0 notice
  option httpchk
  timeout server 10m
  timeout client 10m
EOF

servers=($(echo "$DB_SERVERS" | tr ',' '\n'))
if [ -z "${servers[0]}" ]; then
    echo "Please specify at least one DB server ip/hostname in \$DB_SERVERS"
    exit 1
fi
echo "  server db1 ${servers[0]}:3306 check port 9200" >> $HAPROXY_CONF
if [ "${servers[1]}" ]; then
  echo "  server db2 ${servers[1]}:3306 check port 9200 backup" >> $HAPROXY_CONF
fi
if [ "${servers[2]}" ]; then
  echo "  server db3 ${servers[2]}:3306 check port 9200 backup" >> $HAPROXY_CONF
fi

cat $HAPROXY_CONF

exec /docker-entrypoint.sh "$@"
