temp=input("Enter p,q,r Values:")
p,q,r=temp.split(" ")
a=int(p)
b=int(q)
c=int(r)
d=(b**2)-4*a*c
root1=(-b+(d**0.5))/2*a
root2=(-b-(d**0.5))/2*a
print(f"Roots:({root1},{root2})")
