from fastapi import FastAPI
from routes.v1.metrics import metrics_out
import socket

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/metrics")
async def fetch_metrics(metric: str):
    return metrics_out(
        host=socket.gethostname(),
        metric_type=metric,
    )
