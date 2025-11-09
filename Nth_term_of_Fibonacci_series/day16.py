#Nth term of Fibonacci series

n = int(input("Enter the term number: "))
a, b = 0, 1
for i in range(n):
    a, b = b, a + b
print("The", n, "th term of the Fibonacci series is:", a)
