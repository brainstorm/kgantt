#!/usr/bin/env python

from googlegantt import GanttChart, GanttCategory
from datetime import datetime
import requests
import sys

# FOauth.org credentials
fuser = open(".fuser").read().rstrip()
fpasswd = open(".fpasswd").read().rstrip()

foauth_prefix = 'https://foauth.org/'
trello_url = foauth_prefix+'api.trello.com/1/members/me/boards'
trello_card = foauth_prefix+'api.trello.com/1/cards/6MFWnC2r'

r = requests.get(trello_card, auth=(fuser, fpasswd))

# "2013-02-28T07:00:00.000Z"
due_date = r.json['due'].split('T')[0]

date = [int(i) for i in due_date.split('-')]
today = datetime.now().isocalendar()

gc = GanttChart('Trello Gantt chart', width=650, height=200, progress=(today[0], today[1], today[2]))

on_time = GanttCategory('On Time', '0c0')
late = GanttCategory('Late', 'c00')
upcoming = GanttCategory('Upcoming', '00c')

# Python task finishes one month later after its start date (note date[1]+1)
t1 = gc.add_task('Python task', (date[0], date[1], date[2]), (date[0], date[1]+1, date[2]), category=late)

# Specifying tasks dependencies. Duration specified in days... can be adapted to datetime deltas
t2 = gc.add_task('Kraulis task', depends_on=t1, duration=3, category=upcoming)
t3 = gc.add_task('Valentine task', depends_on=t2, duration=2, category=on_time)

url = gc.get_url()
image = gc.get_image("test_gantt.png")


# XXX: For loop that goes through all boards and fetches the times.
# XXX: The card should be aware on which list is in (different than list "Done" means TODO).
#		isDone() method for cards.
# XXX: Check checklist for each card and search for "Depends on" keyword.
#	Potentially use: http://ipython.org/ipython-doc/dev/parallel/dag_dependencies.html
