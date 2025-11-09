# Armstrong number in a given range

print("Enter the range (start and end) to check for Armstrong numbers:")
start = int(input("Start: "))
end = int(input("End: "))

print("Armstrong numbers between", start, "and", end, "are:")
for num in range(start, end + 1):
    temp = num
    sum = 0
    while temp > 0:
        rem = temp % 10
        sum = sum + rem ** 3
        temp = temp // 10
    if sum == num:
        print(num)
