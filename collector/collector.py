from datetime import datetime
from influxdb import InfluxDBClient
import psutil
import socket
import json
import time

# Setup database client
client = InfluxDBClient(host='influxdb', port=8086)

client.switch_database('collector_metrics')

# defines the hostname where the metrics are running
# to be used as a tag in the database for querying
host = socket.gethostname()

while True:
    # Increment of metrics shipped
    time.sleep(1)

    # Metrics collected listed here
    time_val = datetime.now().isoformat(' ')

    # CPU Related
    cpu_val = psutil.cpu_percent(interval=1)

    # Memory Related
    mem_val = psutil.virtual_memory().percent
    swap_mem_val = psutil.swap_memory().percent

    # Disk Related
    disk = psutil.disk_usage('/')
    disk_percent = psutil.disk_usage('/').percent

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

    # Swap Memory Percent Metrics
    swap_mem_payload = [
        {
        "measurement": "swap_mem_percent",
        "tags": {
            "host": host
        },
        "time": time_val,
        "fields": {
            "value": swap_mem_val
        }
    }
    ]

    # Disk Metrics
    disk_space_percent_payload = [
        {
        "measurement": "disk_percent",
        "tags": {
            "host": host
        },
        "time": time_val,
        "fields": {
            "value": disk_percent
        }
    }
    ]

# Writing data to influxdb
    client.write_points(cpu_payload)
    client.write_points(mem_payload)
    client.write_points(swap_mem_payload)
    client.write_points(disk_space_percent_payload)