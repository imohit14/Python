# Find the Sum of The First N Natural Numbers in Python

print("Enter number to find the sum")

num = int(input())

sum = 0
for i in range(1, num+1):
    sum = sum+i
print(f"The sum of the number is:{sum}")
