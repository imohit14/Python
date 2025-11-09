# Palindrome number

print("Enter number to check palindrome")
num = int(input())
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //=10
    if reverse == num:
        print("Palindrome")
    else:
        print("Not Palindrome")
