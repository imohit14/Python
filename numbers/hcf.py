num1 = int(input("Enter the forst number:"))
num2 = int(input("Enter the second number"))

if num1>num2:
    minm= num2
else:
    minm=num1

for i in range(1, minm+1):
    if num1%i == 0 and num2%i ==0:
        hcf = i
print(f"HCF: {hcf}")