n = int(input("Enter number: "))

if n > 1 and n <= 100:
    A = [0, 1]
    for i in range(1, n+1):
        A.append(A[-1] + A[-2])
    print(A[:n])
else:
    print("Please enter a number which is not greater than 100")