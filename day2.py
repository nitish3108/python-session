'''
	* name the variable properly
	file name should also be in snake case 
	recap:
		data_type {int float string ''/""}
		boolean
		logical_operator
		numerical
		if else and elif
		while loop
'''

#date: 					09-08-2023
'''
	range(n)		//range from 0 to n-1
	range(1, n)		//range from 1 to n-1
	range(1, n, 2)		//range(start, stop, step_size)  1, 3, 5, 7, 9
	we can't give step_size as float
'''
#for i in range(10):
#	print(i)
#

#for i in range(1, 10):
#	print(i)

#for i in range(1, 10, 2):
#	print(i)


'''
	for i in [iterator]:
	every time loop runs it will take one by one value from the iterable
	e.g.,
		x = 'abcdefgh'
		for c in x:
			print(c)
'''
#x = 'abcdefgh'
#for c in x:
#	print(c)

'''
functions are not a first class citizen which means function is of a type. 
If everybuddy is first class citizen then all are equal so we can use function as variable too. 
'''

#how to learn a language
'''
	* Syntax
	* Declaration
	* Looping and other things which we know
	* Start using it
	* Basic library
	* Start basic implementation
'''
#Q. Can we redefine a std. function with my defination and call that function what will be the output 
'''
						list
					--------------------
		syntax - mark = [1, 2, 3, 4] of infinite length
		type(mark)
'''
#mark = [ 1, 2, 3, 4 ]
#print(type(mark))
'''
	list can be indexed in the same way as array
	mark[0]
		in python i, j = 10, 20 => i = 10; j = 20;
'''
number = [1, 2, 3, 4, 5]
#print(type(number))
#for i in range(len(number)):
#	print(number[i])

#for i, j in enumerate(number):
#	print(i, j)
''' immutability : tupple is immutable we can't change its value '''
''' list are mutable so it can be modified whereas tupls can't be modified'''
''' Tupple can be created as ''' 
#x = (1, 2, 3, 4)
#print(type(x))
#print(x[1])
#we can not do following operation
# x[1] = 3
''' 
				 ------------------------------------------------------
				|	 DO NOT MIX 2 TYPE OF DATA IN LIST	       |
				 ------------------------------------------------------
list allows us to reassign anything 
'''
# name = (a, b, c)		//error a,b,c are variables
# a = 1
# name = (a, a, a)
# a = 2
# print(name)		//o/p is name = (1,1,1) it will not reassign that old value

'''
					reversed function
				----------------------------------
		for i in reversed(range(1,0))
			print(i)
						append
				----------------------------------
		append always adds at the last place

						insert
				----------------------------------
		names.insert(index, value) 	#we also have negative index in python 
				
					array splicing
				__________________________________
			name[start_index:end_index] excluding end
			name[start:]			// from stat_index to end
			name[:end_index]		//from 0th to defined index
			#name[-1:-3] 			//reverse slicing not possible so wrong
			
			name[-3:-1]
'''
# Q. list of numbers/digits (single digit +ve number) '''add 1 to the number and return'''

