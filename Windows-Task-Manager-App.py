import time
import psutil
import csv
import os
import datetime

# minutes = time interval between data collection iterations
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

