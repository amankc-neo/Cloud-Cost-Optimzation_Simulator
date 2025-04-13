# Cloud Cost Optimizer (Simulated)

Simulated cost optimization engine that mimics AWS & Azure metrics using local Virtualboc VMs

## Tech stack

- Python
- psutil(for metrics)
-JSON logs
-VirtualBox (simulating VM Usage)

##Features

- Simulates CPU, RAM, Disk, Network usage from VMs
- Stores usage logs in 'simulation/usage_logs/'
- Can be extended with cost estimation & optimization engine

## Run Locally

pip install -r requirements.txt
python simulation/vm_metrics_collector.py


Logs will be generated every 60 seconds
