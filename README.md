# ☁️ Cloud Cost Optimizer (Simulated)

A fully simulated **Cloud Cost Optimization system** that mimics AWS and Azure cost monitoring, resource waste detection, and cost visualization — without needing actual cloud infrastructure.

This is ideal for DevOps learners, cloud engineers without active cloud accounts, or anyone looking to showcase **real-world cloud cost skills** on local VMs (like Oracle VirtualBox).

---

## 📦 Features

### ✅ VM Metrics Collection
- Collects CPU, memory, disk, and network metrics every minute
- Uses `psutil` to simulate a cloud monitoring agent

### 💰 Cloud Cost Estimation
- Applies mocked AWS/Azure pricing to estimate daily cloud costs
- Cost Components:
  - CPU: $0.02 per 1% per hour
  - Memory: $0.01 per GB/hour
  - Disk: $0.005 per GB/hour
  - Network: $0.001 per MB/hour

### ♻️ Waste Optimization Engine
- Flags underutilized VMs:
  - CPU < 5%
  - Memory < 20%
  - Idle for 15+ minutes
- Suggests scale down or shutdown actions

### 📈 Cost Dashboard
- Line chart showing cost trends over time
- Built with `matplotlib`

### 🛠️ Automation Scripts
- `cleanup_old_logs.sh`: Deletes logs older than 7 days
- `run_every_minute.sh`: Simulates cron jobs for end-to-end pipeline

---

## 🧠 Why This Project?

Many developers lack access to AWS/Azure accounts or billing data. This project simulates that experience:
- Recreates a cloud-like environment using VirtualBox
- Teaches how to measure, analyze, and optimize cost
- Prepares you for FinOps, SRE, and DevOps engineering roles

---

## 📁 Folder Structure
```
cloud-cost-optimizer-simulated/
├── simulation/           # VM metric collection
├── estimator/            # Cost estimation logic
├── optimizer/            # Optimization engine
├── dashboard/            # Cost trend visualization
├── scripts/              # Cleanup & runner scripts
├── data/mock_usage_logs/ # Stored logs
├── requirements.txt
└── README.md
```

---

## ▶️ Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start collecting metrics
```bash
python simulation/vm_metrics_collector.py
```

### 3. Estimate cost
```bash
python estimator/cost_estimator.py
```

### 4. Run optimizer
```bash
python optimizer/auto_optimizer.py
```

### 5. View cost trend chart
```bash
python dashboard/cost_dashboard.py
```

### 6. Run full loop + cleanup
```bash
bash scripts/run_every_minute.sh
bash scripts/cleanup_old_logs.sh
```

---

## 🌍 Demo (Screenshots)
*Add screenshots of CLI output and matplotlib charts here.*

---

## 📘 License
MIT License. Use it, modify it, share it.

---

## 🙌 Contributions & Feedback
PRs welcome! For suggestions or questions, feel free to open an issue or connect on [LinkedIn](https://linkedin.com/in/amankc-neo)

---

**Made with 💡 by Aman Choudhary**
