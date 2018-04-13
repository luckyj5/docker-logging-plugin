#!/usr/bin/env bash

cd /go/docker-logging-plugin



sleep 60

# Start docker plugin
./plugin/rootfs/bin/splunk-log-plugin &

echo "Running integration test..."
nodejs ci/run.js
