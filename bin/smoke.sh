#!/usr/bin/env bash

set -e

URL="http://sensors.kevin.colyar.net"

for i in {1..10}
do
    curl -X POST -H "Content-Type: application/json" \
        -d '{"data": ":1640995229697:'Temperature':90.0"}' \
        $URL/v1/temp
    echo ""
    curl -X POST -H "Content-Type: application/json" \
    -d '{"data": "365951380:1640995229697:'Temperature':58.48256793121914"}' \
    $URL/v1/temp
    echo ""
done

curl $URL/v1/errors
echo ""
curl -X "DELETE" $URL/v1/errors
echo ""
curl $URL/v1/errors
