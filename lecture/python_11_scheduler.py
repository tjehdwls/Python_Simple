# 스케쥴러
# - 정해진 시간에 동작하도록 프로그램을 스케줄링
# 5초마다 한번씩
# 특정 일에 한번
# 하루에 한번


# apscheduler
# 1. blocking
# 2. background
import time
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

def print_now():
    print(datetime.now())

def print_love():
    print("I LOVE YOU")


# 1. 스케줄러 생성
# scheduler = BlockingScheduler()
scheduler = BackgroundScheduler()
# 2. 스케줄러 등록(일, 주기, 5초)
# - date: 특정일, 트정날짜에만 동작
# - interval: 간격별로(5초 10분 1시간)
# - CRON: 만능(매일 특정시간에)
scheduler.add_job(print_now, "interval", seconds = 5)
scheduler.add_job(print_love, "cron", hour=13, minute=18)
# 3. 스케줄러 실행
scheduler.start()


#임의 주연 지정
while True:
    time.sleep(1)