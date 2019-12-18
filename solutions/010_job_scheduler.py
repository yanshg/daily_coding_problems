#!/usr/bin/python

"""
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

"""

import threading, time

def print_time():
    print(time.ctime())

def job_sched_with_sleep(f,n):
    print("job_sched_with_time_sleep")
    time.sleep(float(n)/1000)
    f()


def job_sched_with_Timer(f,n):
    print("job_sched_with_threading_Timer")
    t=threading.Timer(float(n)/1000,f)
    t.start()

job_sched_with_sleep(print_time,1000)
job_sched_with_Timer(print_time,1000)
