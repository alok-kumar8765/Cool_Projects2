import imp
from apscheduler.schedulers.blocking import BlockingScheduler
from what import send

def job_func():
    print('hello')

sch = BlockingScheduler()
# sch.add_job(job_func,'interval',hours=2)
sch.add_job(send,'interval',hours=2)

sch.start()
