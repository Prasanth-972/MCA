pi=3.14
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>=b and a>=c:
    n=a
elif b>=a and b>=c:
    n=b
else:
    n=c
nn=n**2
nnn=n**3
result=n+nn+nnn
print(f"n+nn+nnn={n}+{nn}+{nnn}={result}")
r=n
area=pi*r*r
perimeter=2*pi*r
print("Radius of a circle:",r)
print("Area of circle:",area)
print("Perimeter of circle",perimeter)