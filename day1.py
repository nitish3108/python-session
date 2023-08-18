'''
				variable:
		* name = "Anvation" or 'Anvation'		//strings which holds number of characters
	variables name is case sensitive so we need to enter the variable as per case defined
	in python2 we have to use unicode to have multilingual input
		* founding_year=2017	//integer
		* age = 6.5		//float
		age = 'five'		//valid 
	dataType of the varibale is variable for python

	preferred: have a variable to assign data to same type

Naming of variable: all small cases seperated with '_'
e.g., your_name = 'nitish'
	Anything within quotes are treated as strings 
		
		* data = True or data = False		 //boolean
'''

name = 'hello "sagar"'
print(name)
another_name = 'hello\'world'
print(another_name)
name=chr(70)
print(name)

'''
if else condition
	if <condition_1>:
		print("do something")
	elif <condition_2>:
		print("if above is false check this condition")
	else:
		print("do something if condition is false")
'''


is_alive=False
age = 15
if is_alive:
	if age > 85:
		print("alive")
	else:
		print("Enjoy the life")
else:
	print("You are gone!!!!")

'''we can write something similar
'''
if is_alive and age > 85:
	print("Death is near")
elif is_alive and age <= 85:
	print("Enjoy the life")
else:
	print("You are gone!!!")

if not is_alive or age > 85:
	print("it is meaningless")

#Note: '''we will see how to sort the condition as per truth table'''

a = 10 
b = 5 
print( a + b )
print( a - b )	
print( a * b )	# multiply a*b
print( a / b )	# devide and print float
print( a // b )	#be in same data type
print( a ** b)  # a^b
print( a % b )	# Gives remainder 

a = 1
while a <= 10:
	print (a, a*a)
	a += 1

#Duck Taping
'''
	take a loop form 1 to 100, if a number/3 print print """Three""", number/5 print """Five""" else same number 
'''

















