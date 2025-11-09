# Sum of digits of a number

print("Enter a number")
num = int(input())
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
print("Sum of digits is", sum)