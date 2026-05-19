import time 

wait_time = 1
max_retries = 6
attempt = 0

while attempt <max_retries:
    time.sleep(wait_time)
    print("attempt ",attempt+1 , " - and wait time is :",wait_time)
    wait_time = wait_time*2
    attempt = attempt+1