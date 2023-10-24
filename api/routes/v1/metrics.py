import socket
from dependencies.metrics import metrics_out

# defines the hostname where the metrics are running
# to be used as a tag in the database for querying
host = socket.gethostname()


# print(metrics_out(host=host, metric_type="mem"))
# print(metrics_out(host=host, metric_type="cpu"))
# print(metrics_out(host=host, metric_type="disk"))
# print(metrics_out(host=host, metric_type="swapmem"))
