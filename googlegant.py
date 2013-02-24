#!/usr/bin/env python

from googlegantt import GanttChart, GanttCategory
from datetime import datetime
import requests
import sys

# Trello application developer key and token
# Available from: https://trello.com/1/appKey/generate#
key='key='+open(".key").read().rstrip()
token='token='+open(".token").read().rstrip()


trello_url = 'https://api.trello.com/1/members/me/boards'+'?'+key+'&'+token
trello_card = 'https://api.trello.com/1/cards/6MFWnC2r'+'?'+key+'&'+token

r = requests.get(trello_card)
# "2013-02-28T07:00:00.000Z"
due_date = r.json['due'].split('T')[0]

date = [int(i) for i in due_date.split('-')]
today = datetime.now().isocalendar()

gc = GanttChart('Trello Gantt chart', width=650, height=200, progress=(today[0], today[1], today[2]))

on_time = GanttCategory('On Time', '0c0')
late = GanttCategory('Late', 'c00')
upcoming = GanttCategory('Upcoming', '00c')


t1 = gc.add_task('Python task', (date[0], date[1], date[2]), (date[0], date[1]+1, date[2]), category=late)
t2 = gc.add_task('Kraulis task', depends_on=t1, duration=3, category=upcoming)
t3 = gc.add_task('Valentine task', depends_on=t2, duration=2, category=on_time)

url = gc.get_url()
image = gc.get_image("test_gantt.png")


# XXX: The card should be aware on which list is in (different than list "Done" means TODO).
# XXX: For loop that goes through all boards and fetches the times.
# XXX: Check checklist for each card and search for "Depends on" keyword.
# XXX: Check with status of trello support on fopen.org to simplify all the OAuth phase.
