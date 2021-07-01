#This is an draft programme that is meant to mimic AI intergrated softwares in different Operating Systems

from datetime import datetime


print ('Hello, \n \nGoodMorning Sir Dennis.')

first_name = 'Dennis'
last_name = 'Ngethe'
print (input ('How are you doing this fine morning? ' + first_name + ' ' + last_name))

print ('Am doing fantastic, thankyou for asking. \n')

from datetime import datetime, timedelta

today = datetime.now()
one_day = timedelta (days=2)
tomorrow = today + one_day
current_date = datetime.now()

print ('Today is: ' + str(current_date))

today = datetime.now()
print ('The time now is: ' + str(current_date))

print ('You have your dentist appointment on the: ' + str(tomorrow.day) + 'th of june.')

second_name = 'Lucas'
third_name = 'Mwangi'

print ('Mr ' + second_name + third_name + ' wants to discuss the current environmental changes to the new offices')


today = datetime.now()
one_day = timedelta (days=0)
tomorrow = today + one_day
print ('The discussion is to begin at:' + str(current_date.tomorrow))








