def Add(a,b,op):
    if op == "+":
        print (a+b)
    if op == "-":
        print (a-b)
    if op == "*":
        print (a*b)
    if op == "/":
        print (a/b)

while True:
    operators=("+-*/")
    try:
        a = int(input("Enter a number:"))
        op = input ("Enter an operator")
        b = int(input("Enter a number again"))
        if op not in operators:
            print ("What you eneterd is not an operator I can execute")
            exit()
    except ValueError:
        exit()
