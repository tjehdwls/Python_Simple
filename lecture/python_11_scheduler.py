# 스케쥴러
# - 정해진 시간에 동작하도록 프로그램을 스케줄링
# 5초마다 한번씩
# 특정 일에 한번
# 하루에 한번


# apscheduler
# 1. blocking
# 2. background

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def print_now():
    print(datetime.now())

# 1. 스케줄러 생성
scheduler = BlockingScheduler()
# 2. 스케줄러 등록(일, 주기, 5초)
scheduler.add_job(print_now, "interval", seconds = 5)
# 3. 스케줄러 실행
scheduler.start()