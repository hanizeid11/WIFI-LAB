# Iperf Testing and Data Extraction Repository

Welcome to the Iperf Testing and Data Extraction Repository. This repository contains tools and scripts to perform network performance tests using Iperf, and to extract and analyze the results. The repository is organized into three main folders:

1. **Iperf Testers**
2. **Extract Statistics**
3. **Iperf Tests**

## Repository Structure

### 1. Iperf Testers

This folder contains bash scripts to run Iperf tests for different scenarios. There are three scripts available:

- **TCP Test:** `TCP_Test.bat`
- **UDP Test:** `UDP_Test.bat`
- **UDP 50 Mbits/sec Test:** `UDP50_Test.bat`
- **UDP 100 Mbits/sec Test:** `UDP100_Test.bat`

Each script is designed to initiate Iperf tests for the specified protocol and settings. The tests measure the performance of the network, capturing data for both the sender and receiver.

### 2. Extract Statistics

This folder contains Python scripts that extract statistics from the Iperf test results. There are three scripts, each corresponding to the Iperf tests:

- **Extract TCP Statistics:** `TCP_Statistics.py`
- **Extract UDP Statistics:** `UDP_Statistics.py`

These scripts parse the output data from the Iperf tests and extract relevant metrics for analysis.

### 3. Iperf Tests

This folder holds the raw data files from the Iperf tests. The data is organized into subfolders for each test type, and further into sender and receiver data:

- **TCP Data:** `TCP/`
  - `sender/`
  - `receiver/`
- **UDP Data:** `UDP/`
  - `sender/`
  - `receiver/`
- **UDP 50 Mbits/sec Data:** `UDP50/`
  - `sender/`
  - `receiver/`
- **UDP 100 Mbits/sec Data:** `UDP100/`
  - `sender/`
  - `receiver/`


