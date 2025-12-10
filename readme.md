## **Project Requirement **
### **1. Read Nginx Log Files**

Create a Python script named **`read_log.py`** that reads Nginx access log files from a given source directory.

Example usage:

```
python read_log.py --source="/var/log/nginx/access.log"
```

---

### **2. Detect Incremental Log Entries**

The script should identify **only new log lines** since the last read.

* Compare timestamps or track the last processed position (offset).
* Only extract the incremental/remaining log entries.
---

### **3. Store Incremental Data**

Store the newly extracted log data in a **time-series database** (like InfluxDB, TimescaleDB, or Prometheus TSDB).

* Each log entry should be stored with its timestamp.
* Ensure efficient and scalable write operations.