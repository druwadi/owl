# Docker compose is the preferred method -- may scrap this script
echo "Building and running database host"
docker build -f db.Dockerfile . -t testdb
docker run -d -p 8086:8086 testdb
echo "Database started..."
sleep 10
curl -i -XPOST http://localhost:8086/query --data-urlencode "q=CREATE DATABASE collector_metrics"
echo "Building and running test host"
docker build -f host.Dockerfile . -t testhost
docker run -it -d testhost
echo "Test host is running..."

