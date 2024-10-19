n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))
n3 = int(input("Enter the third number : "))

if (n1>n2 & n1> n3):
    print("The number ",n1," is the greatest")
elif(n2>n1 & n2>n3):
    print("The number ",n1," is the greatest")
else:
    print("The number ",n3," is the greatest")