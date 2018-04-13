#!/usr/bin/env bash
export SHELL=/bin/bash

set -e

echo "Running functional tests"

# Start the Docker plugin
./plugin/rootfs/bin/splunk-log-plugin &

# python -m pytest \
# 	--splunkd-url https://splunk-hec:8089 \
# 	--splunk-user admin \
# 	--splunk-password changeme \
# 	--splunk-hec-url https://splunk-hec:8088 \
# 	--splunk-hec-token 00000000-0000-0000-0000-000000000000 \
# 	--docker-plugin-path /splunk/plugin/rootfs/bin/splunk-log-plugin \
# 	--fifo-path /splunk/plugin/pipe
