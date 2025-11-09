#Fibonacci series up to n terms

n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci series:")
for i in range(n):
    c = a + b
    a = b
    b = c
    print(c, end=" ")

    
