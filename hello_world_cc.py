#This program will ask for a name and welcomes the user ("Hello XY").
#If there's no name given, it welcomes the World ("Hello World").

import sys

def Hello():
	if len(sys.argv) > 1:
		print("Hello ",sys.argv[1])
	else:
		print("Hello World")

Hello()
