#The numerical data of which we input into our variables can be used.
#As strings so as to create a specific output


first_num = 8
second_num = 3

print (first_num + second_num)
print (first_num - second_num)
print (first_num * second_num)
print (first_num / second_num)

#Inputing Values
first_num = input ('Please Enter Number')
second_num = input ('Please Enter second Nuber')
print (float(first_num) + int(second_num))

print ('\n')

#Dates
days_in_march = 31

print (str(days_in_march) + ' total days in March')


#To get current date and time we need to use the datetime library
from datetime import date, datetime

current_date = datetime.now()
#The now function returns current date and time as a datetime object 
#For you to concatenate two objects to become one, you must a string on one of the variables

print ('Today is: ' + str(current_date))
