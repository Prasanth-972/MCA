d=int(input("Enter an day:"))
m=int(input("Enter the month:"))
y=int(input("Enter the year:"))
print(f"Entered date:{d:02d}-{m:02d}-{y}")
if(y%4==0):
    print(y,"is leap year")
else:
    print(y,"is not leap year")