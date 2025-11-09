# Armstrong number

print("Enter the number to check")
num = int(input())
temp = num
sum = 0
while temp > 0:
    rem = temp % 10
    sum = sum + rem ** 3
    temp = temp // 10
if sum == num:
    print("Armstrong")
else:
    print("Not Armstrong")
