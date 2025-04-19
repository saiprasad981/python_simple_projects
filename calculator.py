a=input()
x,y=a.split(" ")
p=int(x)
q=int(y)
print("Choose Options: 1.Addition 2.Subtraction 3.Multiplication 4.Divison 5.remainder 6.Floor_division ")
z=int(input("Enter Your Option:"))
if z==1:
    print(f"Addition:{p+q}")
elif z==2:
    print(f"Subtraction:{p-q}")
elif z==3:
    print(f"Multiplication:{p*q}")
elif z==4:
    print(f"Division:{p/q}")
elif z==5:
    print(f"Remainder:{p%q}")
elif z==6:
    print(f"Floor_division:{p//q}")
else:
    print("You Selected Wrong Option")
