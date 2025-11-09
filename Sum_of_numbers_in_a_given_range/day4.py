# Sum of the number in a given range

print("Enter the start of the range.")
start = int(input())
print("Enter the end of the range")
end = int(input())
sum = 0

for i in range(start, end+1):
    sum += i
print(f"The sum of the numbers in the range is: {sum}")
