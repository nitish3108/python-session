#					date: 21/08/2023
#		------------------------------------------------------------------
#			we can not add default argument in the mid of multiple argument of any function
#			def add(a, b=2, c=3):
#				print(a+b+c)
#
#			add(10, b=20, b=80)	//illigal as named and positional argument are mixed
#						//if you start named after that no more position
#			def add(a, b=2, c=3, d=2, e=5, f=0):
#				print(a+b+c)
#
#			add(10, b=20, e=20)	//illigal as named and positional argument are mixed
#						//if you start named after that no more position
#.join e.g., ",".join(string)
'''
	"".".join(string)" joins the string with specified character
	it will join my iterables with specified here it will join with "."

	file operations:- 
		* reading
		* writing
		* append
	

	Reading a File:	
	----------------------------------------------------------------------------------------
		* open("/path/of/the/file")	# built in function to open a file
'''
#
#ifh = open("input_file.txt") 	#it will open in read mode
#print(ifh)
#
#for x in ifh:
#	print(x, end="", sep=",")
#
#ifh.close()
#print(type(ifh))
#

#ifh = open("input_file.txt") 	#it will open in read mode
#ofh = open("copy_file.txt", "w")
#
#print(ifh)
#
#for x in ifh:
#	print(x, end="", sep=",")
#	ofh.write("Hello I read This:\n\t%s" %(x))
#
#ifh.close()
#print(type(ifh))

'''
strip-> it removes widespace character from line
 x = "\n Name with new line \n\n"
 print(x)
 print(x.strip())
	#rstrip() 
	#lstrip()
'''

#Question:
#--------------------
#	
#
#
#
