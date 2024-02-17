import csv
import matplotlib.pyplot as plt
import os
import time
from datetime import datetime as dt

DATA_DIR = "data"

def main():

    roasts = {}

    for filename in os.listdir(DATA_DIR):
        data = {}
        data['time'] = []
        data['temp'] = []
        with open(os.path.join(DATA_DIR, filename), 'r') as f:
            for row in csv.DictReader(f):
                t = time.strptime(row['time'], "%M:%S")
                data['time'].append(t.tm_min * 60 + t.tm_sec)
                data['temp'].append(int(row['temp']))
            roasts[filename] = data

    for label, roast in roasts.items():
        plt.plot(roast['time'], roast['temp'], label=label)

    plt.legend()
    plt.title('SR 800 Roasting Profile')
    plt.xlabel('Time (s)')
    plt.ylabel('Temp (Deg F)')

    plt.savefig(f"sr800_roast_{dt.today()}.png")
    
        

if __name__ == '__main__':
    main()

