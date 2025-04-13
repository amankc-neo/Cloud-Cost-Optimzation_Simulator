import os
import json
from datetime import datetime
import matplotlib.pyplot as plt

LOG_DIR = "data/mock_usage_logs"

PRICING = {
    "cpu_percent": 0.02,
    "memory_gb": 0.01,
    "disk_used_gb": 0.005,
    "network_mb": 0.001
}

def estimate_cost(entry):
    cpu_cost = entry["cpu_percent"] * PRICING["cpu_percent"] / 100
    mem_used_gb = entry["memory"]["used"] / (1024 ** 3)
    mem_cost = mem_used_gb * PRICING["memory_gb"]
    disk_used_gb = entry["disk"]["used"] / (1024 ** 3)
    disk_cost = disk_used_gb * PRICING["disk_used_gb"]
    network_mb = (entry["network"]["bytes_sent"] + entry["network"]["bytes_recv"]) / (1024 ** 2)
    net_cost = network_mb * PRICING["network_mb"]
    return cpu_cost + mem_cost + disk_cost + net_cost

def gather_cost_data():
    daily_costs = {}
    for file in sorted(os.listdir(LOG_DIR)):
        if not file.endswith(".json"):
            continue
        date_str = file.split("_")[-1].replace(".json", "")
        with open(os.path.join(LOG_DIR, file), 'r') as f:
            logs = json.load(f)
            total = sum(estimate_cost(entry) for entry in logs)
            daily_costs[date_str] = round(total, 2)
    return daily_costs

def plot_cost_trend():
    data = gather_cost_data()
    if not data:
        print("[!] No log data available.")
        return

    dates = list(data.keys())
    costs = list(data.values())

    plt.figure(figsize=(10, 5))
    plt.plot(dates, costs, marker='o', linestyle='-', color='green')
    plt.title("📉 Cloud Cost Trend (Simulated)")
    plt.xlabel("Date")
    plt.ylabel("Cost ($)")
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    plot_cost_trend()
