#						Date: 16/08/2023
#					________________________________

''' 
	In unpacking a tuple we need to match number of argument

	e.g., x = (1,2)
		a,b = x		# valid

		a, b, c = x	# invalid

	e.g.2, x = (1, 2, 3)
		a, b = x	# invalid
		a, b, c = x	# valid

'''

#def get_votar_id(eligible_status, valid_votar):
#	if_eligible = eligible_status
#	votar_id = valid_votar
#
#	return if_eligible, votar_id
#
#status, votar_id = get_votar_id(False, 'No')
#
#def function_call():
#	get_votar_id(False, 'Yes')
#if status:
#	print("Do what ever you want to do")

'''
	None is nothing if some variable is unknown we can initialize the var with 'None' which can we later updated to any type
'''

#name = None
#
#def green_function(name="green"):
#	print("Your name is" + name)

'''
	Traversing:
		time complexity denoted with O(n) can be read as bigO of n

	we use dictionary where we can mount the value with respect of their key
	syntax:
	-----------
		my_dictionary = {}

		insertion => 
			my_dictionary[key] = value
		 ________________________________________________________________________
		|	in dictionary anything can be index which is *hashable*		 |
		 ------------------------------------------------------------------------ 
	
	Q. How can we recover the the value from a hashmap if key collission occured?
		
		e.g., 
			a = {'a': 10, 'b': 20, 'c': 30}
			a['a']

			a[d] = 40
'''
# iterating the dictionary

#a = {'a': 10, 'b': 20, 'c': 30}
#for e in a:
#	print(e, a[e])
#

#is/in/none/dictionary 

#* find_pair function
#	find_pair(input, target)	//input is list may/maynot be sorted * 
#			from the input list find pair whose sum is equal to target
#			if sum not exist return empty tuple *
# time complexity should be of O(n)

