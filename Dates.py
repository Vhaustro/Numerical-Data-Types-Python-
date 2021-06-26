#Dates
#To create and acquire date and time, we need to use the datetime library.
#Get the datetime time function from the datetime library
#from datetime import datetime


#Datetime now 
#datetime.now will return the current date and time
#the now function returns a datetime object

#Functions to use with a date
current_date = datetime.now()
print ('Today is: ' + str(current_date))

today = datetime.now()


#Dates
days_in_march = 31

print (str(days_in_march) + ' total days in March')


#To get current date and time we need to use the datetime library
from datetime import date, datetime

current_date = datetime.now()
#The now function returns current date and time as a datetime object 
#For you to concatenate two objects to become one, you must a string on one of the variables

print ('Today is: ' + str(current_date))


#Timedelta is used to calculate the number of days before "something"
#Used also as a 'timer'

one_day = timedelta(days=1)
yesterday = today - one_day
print ('Yesterday was: ' + str(yesterday))

from datetime import datetime, timedelta
current_date = datetime.now()

print ('Day: ' + str(current_date.day))
print ('Month: '+ str(current_date.day))
print ('Year: ' + str(current_date.day))
#Recieve date as a string and need to convert it to a datetime object

birthday = input ('When is your birthday (dd/mm/yy)? ')
birthday_date= 25
print ('Birthday: ' + str(birthday_date))


#Testing input of Dates - (DEMONSTRATION)

#To get current date and time we need to use the date time library
from datetime import datetime

current_date = datetime.now()
#The now function returns current date and time as a datetime object
#You must convert the datetime object to a string
#Before you can concatenate it to another string
#Concatenate - link things together in a series or chains 

print ('Today is:' + str(today))

print ('Week is: ' + str(week=1))

#Using timedelta allows you to manipulate the dates and times
#You can change, remove or add days weeks to a date (used to specify a period of time)
one_day = timedelta(days=1)

timedelta 

one_week = timedelta(week=1)
last_week = today - one_week
print ('Last week was: ' + str(last_week)


#Formating Dates


#use day, month, year, hour, minute, second functions
#to display only part of the date 
#All of these functions return intergers
#Convert them to strings before concatenating them to another string

#Test one of output
print ('Day: ' + str(today.day))
print ('Month: ' + str(today.month))
print ('Year: ' + str(today.year))

#Input of Date and Times
from datetime import datetime, timedelta



