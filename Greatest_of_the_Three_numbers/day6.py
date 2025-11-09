# find greatest of three numbers
print("Enter first number:")
a = int(input())
print("Enter second number:")
b = int(input())
print("Enter third number:")
c = int(input())
print("The greatest number is:", a if a > b and a > c else b if b > c else c)
