#This program will ask for a name and welcomes the user ("Hello XY").
#If there's no name given, it welcomes the World ("Hello World").

import sys
# I used sys.argv to check if anything (name) is entered other than the name of the program
def Hello():
	if len(sys.argv) > 1:
		print("Hello ",sys.argv[1])
	else:
		print("Hello World")

Hello()

