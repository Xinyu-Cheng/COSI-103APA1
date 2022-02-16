'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''

from schedule import Schedule
import sys

schedule = Schedule()
schedule.load_courses()
schedule = schedule.enrolled(range(5,1000)) # eliminate courses with no students

TOP_LEVEL_MENU = '''
quit
reset
term  (filter by term)
course (filter by coursenum, e.g. COSI 103a)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title  (filter by phrase in title)
description (filter by phrase in description)
timeofday (filter by day and time, e.g. meets at 11 on Wed)
limit (filter by upper limit, e.g. 50)
starttime(filter by start time, based on a 24-hour clock)
'''

terms = {c['term'] for c in schedule.courses}

def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global schedule
    while True:         
        command = input(">> (h for help) ")
        if command=='quit':
            return
        elif command in ['h','help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r','reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5,1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            schedule = schedule.term([term]).sort('subject')
        elif command in ['s','subject']:
            subject = input("enter a subject:")
            schedule = schedule.subject([subject])
        #7.a --Jingqian
        elif command in ['c','course']:
            coursenum = input("enter a coursenum:")
            schedule = schedule.coursenum(coursenum)
        #7.e --Jingqian
        elif command in ['l','limit']:
            limit = int(input("enter a limit:"))
            schedule = schedule.limit(range(0, limit))
        elif command in ['d','description']:
            phrase = input("enter a phrase:")
            schedule = schedule.description(phrase)
        #7.b --weidong 
        elif command in ['title']:
            phrase = input("enter a phrase:")
            schedule = schedule.title(phrase)
        #7.e --weidong 
        elif command in ['starttime']:
            time = int(input("enter a start time:"))
            schedule = schedule.starttime(time)
        elif command in ['day']:
            time = input("enter a day(m,tu,w,th,f):")
            schedule = schedule.day(time)
        else:
            print('command',command,'is not supported')
            continue
            
        print("courses has",len(schedule.courses),'elements',end="\n\n")
        print('here are the first 10')
        for course in schedule.courses[:10]:
            print_course(course)
        print('\n'*3)

def print_course(course):
    '''
    print_course prints a brief description of the course 
    '''
    print(course['subject'],course['coursenum'],course['section'],
          course['name'],course['term'],course['instructor'])

if __name__ == '__main__':
    topmenu()

