#					Date: 28/08/2023
#--------------------------------------------------------------------------------------------------
#				Exceptions
#			-------------------------
'''
import os
filename = "absehlsf.txt"

try:
	
	print("Trying to open")
	ifh = open(filename)
	#with open(filename) as ifh:		#while handling file use with
	print("it will not print this")

#except:		#used to catch all the errors
except FileNotFoundError as x:
	print("Exception occured")
	print(type(x))
	print(x)

except ValueError:
	print("Value Error Occured")

#except FileNotFoundError, ValueError:
#	print("something wrong")
#

finally:
	print(ifh.close)
'''

#
