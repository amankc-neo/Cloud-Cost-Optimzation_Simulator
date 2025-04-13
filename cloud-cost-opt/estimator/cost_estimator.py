import os
import json
from datetime import datetime

LOG_DIR = "/home/neo/project/cloud-cost-opt/data/usage_logs"

PRICING = {
    "cpu_percent": 0.02,
    "memory_gb": 0.01,
    "disk_used_gb": 0.005,
    "network_mb": 0.001,
}

def estimate_cost_from_metrics(metrics):
    cpu_cost = metrics["cpu_percent"] * PRICING["cpu_percent"] / 100

    mem_used_gb = metrics["memory"]["used"] / (1024 ** 3)
    mem_cost = mem_used_gb * PRICING["memory_gb"]

    disk_used_gb = metrics["disk"]["used"] / (1024 ** 3)
    disk_cost = disk_used_gb * PRICING["disk_used_gb"]

    network_mb = (metrics["network"]["bytes_sent"] + metrics["network"]["bytes_recv"]) / (1024 ** 2)
    net_cost = network_mb * PRICING["network_mb"]

    total = round(cpu_cost + mem_cost + disk_cost + net_cost, 4)
    return total

def estimate_daily_cost(date_str):
    log_file = os.path.join(LOG_DIR, f"vm_metrics_{date_str}.json")
    if not os.path.exists(log_file):
        print("[!] No logs found for that date.")
        return

    with open(log_file, 'r') as f:
        logs = json.load(f)

    daily_total = 0
    for entry in logs:
        daily_total += estimate_cost_from_metrics(entry)

    print(f"[1] Estimated Total Cost For {date_str}: ${round(daily_total, 2)}")

if __name__ == "__main__":
    today = datetime.utcnow().strftime("%Y-%m-%d")
    estimate_daily_cost(today)

