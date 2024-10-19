principal_amt = int(input("Enter the principal amount : "))
rate = int(input("Enter the annual rate in percentage : "))
time = int(input("Enter the time period : "))

interest = (principal_amt*rate*time)/100
print("Simple interset : ",interest)