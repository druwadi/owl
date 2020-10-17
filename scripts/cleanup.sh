echo 'Running cleanup script to shut down running containers'
echo 'Stopping all running containers...'
docker stop $(docker ps -a -q) 