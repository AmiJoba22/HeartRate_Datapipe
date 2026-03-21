# Heart Rate Data Pipeline 
## Data Engineering Lab Assignment - The Knowledge House 
### The Challenge:
- You are a junior data engineer at a Taiwan-based wearable health-tech firm called Seng-Links. Your company has just discovered that the raw heart-rate exports from prototype devices are inconsistent. Some files contains malformed records, impossible values, or missing entries. Before the machine learning team can study usage and identify sleep & exercise patterns, the data engineering team must build a batch-processing pipeline that reads raw files cleans records, computes quality checks, and calculates descriptive statistics for later analysis.

Your company has provided you a folder named "data/", which contains 4 files of heart-rate samples from one 30 year old participant. The participants device records heart rate every 5 minutes. Your task is to write a Python program that:

## Instructions

There are two Python files which you will modify in this repository to complete this project:
* [main.py](main.py)
* [writeup.md](results/writeup.md)

Once you've completed the coding portion of this project in the `main.py` file and ensured that your output is correct, you will then provide a writeup in the file `writeup.md`, where you will answer analytical questions on the data you've analyzed.

**main.py**

You can run this module by typing and executing the following command in your terminal: 

```
python main.py
```

This module serves as the main data pipeline for your project. It integrates the functions you implemented to read the raw data files (using file I/O), compute descriptive statistics (using for-loops), and generate outputs for your analysis. 

This module contains the following functions:

* `clean_heartrate_data`
* `average`
* `median`
* `range`
* `rolling_avg` (Challenge function)
* `run`
