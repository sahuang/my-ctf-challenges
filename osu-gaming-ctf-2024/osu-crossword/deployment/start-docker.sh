#!/bin/sh
docker container rm -f crossword
docker run -d -p7270:7270 --restart=always --name=crossword --privileged crossword