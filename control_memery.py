import time

import requests
import psutil

memory_threshold = 2147483648  # байт
api_url = 'https://example.com/api/alarm'

while True:
    memory_used = psutil.virtual_memory().used

    if memory_used >= memory_threshold:
        response = requests.post(api_url, data={"message": "High memory usage"})

    time.sleep(600)  # раз в 10 минут
