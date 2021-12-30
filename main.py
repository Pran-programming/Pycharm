a = int(input("enter your first number"))
b = int(input("enter your second number"))


print('Enter:\n"a" if you want to add\n"b" if you want to subtract\n"c"if you want to divide \n"d" if you want to do multiplication \n"e" if you want to square a number')

c = input("Enter your choice: ")

if c == "a":
    d = a+b
    print(a,"+",b,"=",d)
elif c == "b":
    d = a-b
    print(a,"-",b,"=",d)
elif c == "c":
    d = a/b
    print(a,"/",b,"=",d)
elif c == "d":
    d = a*b
    print(a,"*",b,"=",d)
elif c == "e":
    d = a**b
    print(a,"**",b,"=",d)
else:
    print("invalid input")
