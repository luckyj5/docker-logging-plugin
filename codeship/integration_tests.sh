#!/usr/bin/env bash
export SHELL=/bin/bash

set -e

echo "Running integration tests"

# Start the Docker plugin
./plugin/rootfs/bin/splunk-log-plugin &

nodejs ./codeship/integration/run.js
