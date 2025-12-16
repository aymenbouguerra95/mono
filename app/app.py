from flask import Flask, jsonify
import psutil 

app = Flask(__name__)
@app.route("/")
def home():
    return " monotoring tool is running"
@app.route("/status")
def status():
    return {"status":'ok',"service": 'monotoring cpu', "version":'1.0.0'}    
@app.route("/health")
def health():
    data ={
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory()._asdict(),
        "disk": psutil.disk_usage('/')._asdict(),
        "boot_time": psutil.boot_time()
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
