---

## 🛠️ Automation Scripts

### 🧹 `cleanup_old_logs.sh`
Deletes log files older than 7 days.
```bash
bash scripts/cleanup_old_logs.sh
```

### 🔁 `run_every_minute.sh`
Runs all major modules in a loop every minute (simulated cron).
```bash
bash scripts/run_every_minute.sh
```

> You can run this as a background process to simulate 24/7 monitoring like a cloud agent.

