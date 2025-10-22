n = int(input("Enter a number: "))

if n < 1 or n > 1000:
    print("please enter a number between 1 and 1000")
else:
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=" ")