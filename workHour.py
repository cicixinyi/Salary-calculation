""" based on 15min = 0.25h; 
    if ! < 15, work_time = 0; if 15 < ! < 30, work_time = 15min
    8:00 - 11:30  3.5h
    12:00 - 17:30  5.5h
    18:00 - 21:00  3h  """

from datetime import *
def workHour(start,end):
    msh = int(start.split(':')[0])
    msm = int(start.split(':')[1])
    meh = int(end.split(':')[0])
    mem = int(end.split(':')[1])
    print(msh, msm, meh, mem)

    while msm % 15 != 0 or mem % 15 != 0:
        if msm % 15 != 0:
            msm+=1
        else:
            mem-=1

    work = meh + mem / 60 - (msh + msm / 60)
    print(work)
    return work

def fullTime_m():
    return 3.5

def fullTime_a():
    return 5.5

def fullTime_e():
    return 3.0
    
#workHour('8:15','11:00')