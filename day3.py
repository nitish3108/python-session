#						date:  11/08/2023
#				----------------------------------------------
#
'''
						recap
				----------------------------------------------
list = [9,9,0]
carry = 1
for i in range(len(list)-1, -1 -1):
	digit = list[i] + carry
	list[i] = digit % 10
	carry = list[i] // 10

test cases can be written as 
	assert [ expected_output ] == function(argument)
'''

#						functions
#				------------------------------------------------

'''
can we create a variable without initialization? if yes what is the default value of variable assigned to variable?

		def function_name(parameteres):
			#all the required defination which are called regularly
	e.g.,
		def my_custom_length(iterable):
			length = 0
			for i in iterable:
				length = 1
			return length
'''

#def my_custom_len(iterable):
#	length = 0
#	for i in iterable:
#		length += 1
#	return length
#
#outer_length = my_custom_len([1, 2, 3])
#print(outer_length)
#digit = [1, 2, 4]
#print(my_custom_len(digit))
#
#students = ["Ram", "Shyam", "Hari", "Om"]
#maximum_name_length = 0
#for name in students:
#	student_name_length = my_custom_len(name)
#	if student_name_length > maximum_name_length:
#		maximum_name_length = student_name_length 
#print(maximum_name_length)

#assert 5 == my_custom_len("Shyam")

