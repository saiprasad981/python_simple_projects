year=int(input("enter a year:"))
if year %4 ==0:
    if year % 100==0:
        if year % 400==0:print("Leap Year")
        else:print("non leap year")
    else:print("leap year")
else:print("non leap year")