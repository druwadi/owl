import psutil
from dependencies.timing import current_time
from dependencies.tags import fetchTags


def metrics(metric_type: str):
    match metric_type:
        case "disk":
            return psutil.disk_usage("/").percent
        case "cpu":
            return psutil.cpu_percent(interval=1)
        case "mem":
            return psutil.virtual_memory().percent
        case "swapmem":
            return psutil.swap_memory().percent
        case _:
            # TODO fix later
            print("error switching")


def metrics_out(host: str, metric_type: str):
    return str(
        {
            "metrictype": metric_type,
            "tags": [f"{fetchTags(host)}"],
            "timestamp": current_time(),
            "value": metrics(metric_type=metric_type),
        }
    )
