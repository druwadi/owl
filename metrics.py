from datetime import datetime
from influxdb import InfluxDBClient
import psutil
import socket
import json

database = InfluxDBClient(host='localhost', port=8086)

# defines the hostname where the metrics are running
# to be used as a tag in the database for querying
host = socket.gethostname()

while True:
    time = datetime.now()
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    print('Tag: ', host)
    print('Time: ' + str(time))
    print('CPU Percent: ' + str(cpu))
    print('MEM Percent: ' + str(mem))
    