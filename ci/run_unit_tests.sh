#!/usr/bin/env bash

cd /go
go get -t -v ./...

cd /go/docker-logging-plugin

go test