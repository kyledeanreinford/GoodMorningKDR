#! /usr/bin/python3

import webbrowser, calendar
from datetime import date

webbrowser.open('http://gizmodo.com')
webbrowser.open('http://theringer.com')
webbrowser.open('http://espn.com/soccer')
webbrowser.open('http://lifehacker.com')

# todays_date = date.today()
# day_of_week = calendar.day_name[todays_date.weekday()]
# month = todays_date.strftime('%B')
# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# if month.lower() == 'august':
#     month = 'aug'
# if month.lower() == 'september':
#     month = 'sept'
# if month.lower() == 'october':
#     month = 'oct'
# if month.lower() == 'november':
#     month = 'nov'
# if month.lower() == 'december':
#     month = 'dec'
# if month.lower() == 'january':
#     month = 'jan'

# if day_of_week in weekdays:
#     webbrowser.open('https://fivethirtyeight.com/features/significant-digits-for-' + day_of_week.lower() + '-' + month.lower() + '-' + str(date.today().day) + '-' + str(date.today().year))
