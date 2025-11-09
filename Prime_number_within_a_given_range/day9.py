# prime number for a give range
print("Enter the start of range")
start = int(input())
print("Enter the end of range")
end = int(input())
for num in range(start, end+1):
    if start > 1:
        for i in range(2, start):
            if start % i == 0:
                print(start, "is not a prime number")
                break
        else:
            print(start, "is a prime number")