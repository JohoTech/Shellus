#!/usr/bin/env bash

docker pull redis
docker run --name redis -d redis