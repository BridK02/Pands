#messing around with variable types
# author: Brid Kennedy
ageofPatient = {}
age = '3'

#we need to convert the type to str so we can concate it to the message
print ("type of ageofPatient is :" + str(type(ageofPatient)))
print ("type of age is :" + str(type(age)))

print ("you are " + str(age))
nextYear = int(age) + 1
print ("next year you will be " + str(nextYear))