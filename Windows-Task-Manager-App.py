'''
Problem 1
Implement a program that will launcha specified process and periodically (with aprovided time interval) collect the following data about it:
•	CPU usage (percent);
•	Memory consumption: Working Set and Private Bytes (for Windows systems)or Resident Set Size and Virtual Memory Size (for Linux systems);
•	Number of open handles (for Windows systems)or file descriptors (for Linux systems).
Data collection should be performed all the time the process is running. Path to the executable file for the process and time interval between data
 collection iterations should be provided by user. Collected data should best stored on the disk. Format of stored data should support automated
parsing to potentially allow, for example, drawing of charts.
'''
import time
import psutil
import csv
import os
import datetime

def colect_data(minutes=0):
    while True:
        CPU = psutil.cpu_percent(4)
        rss = psutil.Process().memory_info()[0]
        VMS = psutil.Process().memory_info()[1]
        Noh = psutil.Process().num_handles()
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        filenames = [[date,CPU,rss,VMS,Noh]]

        if os.path.exists('CPU data.csv'):
            with open('CPU data.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(filenames)
        else:
            with open('CPU data.csv', 'w', newline='') as f:
                columns = ['date', 'CPU', 'Working Set', 'Private Bytes', 'Number of open handles']
                writer = csv.writer(f)
                writer.writerow(columns)
                writer.writerows(filenames)
        time.sleep(minutes*60)


colect_data(1)

