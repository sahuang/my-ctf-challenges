#!/bin/sh
docker container rm -f tillerino
docker run -d -p7271:7271 --restart=always --name=tillerino --privileged tillerino