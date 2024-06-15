#!/bin/sh
docker container rm -f ppv3
docker run -d -p7272:7272 --restart=always --name=ppv3 --privileged ppv3