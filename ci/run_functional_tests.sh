#!/usr/bin/env bash
export SHELL=/bin/bash
cd /go/docker-logging-plugin


cd test

echo "Creating virtual env to run pytests..."

pip3 install virtualenv
virtualenv --python=python3.5 venv
source venv/bin/activate
pip install -r requirements.txt

echo "Running pytests...."
python -m pytest --splunkd-url https://splunk-hec:8089 --splunk-user admin --splunk-password changeme --splunk-hec-url https://splunk-hec:8088 --splunk-hec-token 00000000-0000-0000-0000-000000000000 --docker-plugin-path /go/docker-logging-plugin/plugin/rootfs/bin/splunk-log-plugin --fifo-path /go/docker-logging-plugin/pipe

echo "!-------------------Done with testing-------------------!"

#Hack to send kill splunk container after testing.
curl -u admin:changeme -k https://splunk-hec:8089/servicesNS/nobody/launcher/configs/conf-inputs -d 'name=batch:///Test-input' > /dev/null 2>&1
