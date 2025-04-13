import psutil
import time
import json
import os
from datetime import datetime

LOG_DIR = "/home/neo/project/cloud-cost-opt/data/usage_logs"
os.makedirs(LOG_DIR, exist_ok=True)

def collect_vm_metrics():
    timestamp = datetime.utcnow().isoformat()
    metrics = {
            "timestamp": timestamp,
            "cpu_percent": psutil.cpu_percent(interval=1),
            "memory": psutil.virtual_memory()._asdict(),
            "disk": psutil.disk_usage('/')._asdict(),
            "network": psutil.net_io_counters()._asdict()
     }
    return metrics

def save_metrics(metrics):
    date_str = datetime.utcnow().strftime("%Y-%m-%d")
    log_file = os.path.join(LOG_DIR, f"vm_metrics_{date_str}.json")

    if os.path.exists(log_file):
        with open(log_file, 'r+') as f:
            data = json.load(f)
            data.append(metrics)
            f.seek(0)
            json.dump(data, f, indent=2)

    else:
        with open(log_file, 'w') as f:
            json.dump([metrics], f, indent=2)

if __name__ == "__main__":
    while True:
        m = collect_vm_metrics()
        save_metrics(m)
        print(f"[1] logged at {m['timestamp']}")
        time.sleep(60)
