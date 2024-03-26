import time

wait_time=1
attempts=0
max_retrives=5

while attempts < max_retrives:
    print("Attempt",attempts+1,"- wait time",wait_time)
    time.sleep(wait_time)
    wait_time *=2
    attempts+=1