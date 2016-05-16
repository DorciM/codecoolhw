import sys
# Some introduction
print "Hey there! I'm a simple calculator. I can only do +,-,*,/"
# Here I defined the operations executed by my program.
# If you try to divide by 0, you'll get a mathematical error, and it stops the prgram.
def Add(num1,num2,op):
    if op == "+":
        print (num1+num2)
    if op == "-":
        print (num1-num2)
    if op == "*":
        print (num1*num2)
    if op == "/":
        if num2 == 0:
            print ("Math Error")
            exit()
        else:
            print (num1/num2)
# Here I used a while loop, and ValueError to handle invalid input
while True:
    operators=("+-*/") #the program will check between the 26-29 lines if the input is an operator
    try:
        num1 = int(input("Enter a number:"))
        op = input ("Enter an operation:")
        num2 = int(input("Enter your second number:"))
        if op not in operators:
            print ("What you eneterd is not an operator I can execute")
            exit()
    except ValueError: #If the input for a or b is not an integer, the program stops here.
        exit()
# Let's do the stuff!
Add(num1,num2,op)
