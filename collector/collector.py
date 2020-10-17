from datetime import datetime
from influxdb import InfluxDBClient
import psutil
import socket
import json

# Setup database client
client = InfluxDBClient(host='influxdb', port=8086)

client.switch_database('collector_metrics')

# defines the hostname where the metrics are running
# to be used as a tag in the database for querying
host = socket.gethostname()

while True:
    # Metrics collected listed here
    time_val = datetime.now().isoformat(' ')
    cpu_val = psutil.cpu_percent(interval=1)
    mem_val = psutil.virtual_memory().percent

    # JSON objects for DB ingestion 

    # CPU Percent Metrics
    cpu_payload = [
        {
        "measurement": "cpu_percent",
        "tags": {
            "host": host
        },
        "time": time_val,
        "fields": {
            "value": cpu_val
        }
    }
    ]

    # Memory Percent Metrics
    mem_payload = [
        {
        "measurement": "mem_percent",
        "tags": {
            "host": host
        },
        "time": time_val,
        "fields": {
            "value": mem_val
        }
    }
    ]
    
    # Debug statements
    #print(cpu_payload)
    #print(mem_payload)

    client.write_points(cpu_payload)
    client.write_points(mem_payload)