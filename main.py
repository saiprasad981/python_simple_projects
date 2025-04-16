a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("enter 1.for addition 2.for subtraction 3.for multiplication 4.for division 5.for remainder :"))
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4:
    print(a/b)
elif c==5:
    print(a%b)
else:
    print("input error")
