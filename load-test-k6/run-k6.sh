#!/bin/sh

echo "Running K6 load test on $url with $vus virtual users for $duration " 1>&2

k6 run --out influxdb=$influxdb_url /script.js > /dev/null

if [ $? -eq 0 ]; then
    echo "Completed load test on $url" 1>&2
    echo "true"
else
    echo "Load test on $url failed" 1>&2
    echo "false"
fi