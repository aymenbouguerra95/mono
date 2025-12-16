from flask import Flask, Response
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST
import psutil

app = Flask(__name__)

cpu_gauge = Gauge('cpu_usage_percent', 'CPU usage percent')
memory_gauge = Gauge('memory_usage_percent', 'Memory usage percent')

@app.route("/")
def home():
    return "Monitoring Tool is running"

@app.route("/metrics")
def metrics():
    cpu_gauge.set(psutil.cpu_percent(interval=1))
    memory_gauge.set(psutil.virtual_memory().percent)

    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
