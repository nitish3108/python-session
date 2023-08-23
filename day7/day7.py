#						Date: 23/08/2023
#---------------------------------------------------------------------------------------------------------
'''
this file is linekd with file name temp.py
'''
'''
def add(first, second):
	return first + second

def sub(first, second):
	return first - second

def main():
	print("printed from main only if you run this file directly")
	print("Will be printed only if you call main function after import")
	print(add(1,2))
	print(sub(2,2))

print( __name__ )	# this will tell weather file is running as module or running as main

if __name__ == '__main__':
	#this part will only run if your program run within same file
	main()
'''
#we can import some directory as well as module

#import assign 
# we need to create a __init__.py file to import a directory as module without that it will not concider directory as module
#we need to specify all file that i want to import in "__init__.py" file

#from assign import add_one_to_number
#from . import temp 	#this can be only done if we are importing something from current dir
