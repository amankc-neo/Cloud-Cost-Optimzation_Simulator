---

## Cost Entimation (Mock)

This module estimates cost using simulated usage logs and mock cloud pricing:

- **CPU**: $0.02 per 1% per  hour
- **Memory**: $0.01 per GB/hour
- **Disk**: $0.005 per GB/hour
- **Network**: $0.001 per MB/hour


### Run Estimator

---
python3 estimator/cost_estimator.py

---

You will see the total estimate cost for today based on the collected logs.
