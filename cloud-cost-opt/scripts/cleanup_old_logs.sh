#!/bin/bash

LOG_DIR="/home/neo/project/cloud-cost-optdata/mock_usage_logs"
DAYS_TO_KEEP=7

find "$LOG_DIR" -type f -name '*.json' -mtime +$DAYS_TO_KEEP -exec rm -v {} \;
echo "[✓] Cleanup complete. Deleted logs older than $DAYS_TO_KEEP days."

