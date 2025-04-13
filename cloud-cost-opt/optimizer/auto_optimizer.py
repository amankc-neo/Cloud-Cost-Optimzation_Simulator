import os
import json
from datetime import datetime

LOG_DIR = "/home/neo/project/cloud-cost-opt/data/mock_usage_logs"
IDLE_CPU_THRESHOLD = 5      # < 5% CPU means idle
IDLE_MEM_THRESHOLD = 0.2    # < 20% memory usage means underutilized
IDLE_DURATION = 15          # if VM stays idle for 15+ mins, flag it

def analyze_logs_for_waste(date_str):
    log_file = os.path.join(LOG_DIR, f"vm_metrics_{date_str}.json")
    if not os.path.exists(log_file):
        print("[!] No logs found for that date.")
        return

    with open(log_file, 'r') as f:
        logs = json.load(f)

    idle_count = 0
    for entry in logs:
        cpu = entry['cpu_percent']
        mem_percent = entry['memory']['percent'] / 100
        
        if cpu < IDLE_CPU_THRESHOLD and mem_percent < IDLE_MEM_THRESHOLD:
            idle_count += 1

    idle_minutes = idle_count  # logs are taken every minute

    if idle_minutes >= IDLE_DURATION:
        print(f"[!] Optimization Suggestion: VM was idle for {idle_minutes} minutes. Consider scaling down or stopping.")
    else:
        print(f"[✓] VM Utilization is healthy. Idle time = {idle_minutes} mins")

if __name__ == "__main__":
    today = datetime.utcnow().strftime("%Y-%m-%d")
    analyze_logs_for_waste(today)
