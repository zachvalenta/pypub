import schedule
import time
import os


def return_something():
    print("Hello world!")


interval = int(os.environ.get('INTERVAL'))
schedule.every(interval).seconds.do(return_something)

while True:
    schedule.run_pending()
    time.sleep(1)
