import threading
import psutil
import time

times = []
thread_calis = True

def monitor_cpu():
    while thread_calis:
        times.append(psutil.cpu_percent())
        time.sleep(0.5)
    
t = threading.Thread(target=monitor_cpu)
t.start()

import math
value = math.factorial(10000)
import requests

requests.get("http://www.duckduckgo.com").text

thread_calis = False
t.join()
print(*times, sep="\n")