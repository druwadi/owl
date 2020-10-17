echo "Starting up InfluxDB via Docker"
docker run -d -p 8086:8086 influxdb:1.8.2
echo "Database started..."
sleep 10
curl -i -XPOST http://localhost:8086/query --data-urlencode "q=CREATE DATABASE collector_metrics"
echo "Building and running test host"
docker build -f host.Dockerfile . -t host
docker run -it -d host /bin/bash
echo "Test host is running..."

