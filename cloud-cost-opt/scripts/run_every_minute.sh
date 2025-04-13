#!/bin/bash

while true; do
    echo "[>] Collecting VM metrics..."
    python3 simulation/vm_metrics_collector.py &
    sleep 60
    pkill -f simulation/vm_metrics_collector.py

echo "[>] Running optimizer..."
    python3 optimizer/auto_optimizer.py

echo "[>] Estimating daily cost..."
    python3 estimator/cost_estimator.py

echo "[>] Done. Waiting for next run..."
    sleep 60

done
