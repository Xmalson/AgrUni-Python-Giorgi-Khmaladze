def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > 10000 or b > 10000 or a < 1 or b < 1:
    print("Invalid input")
else:
    c = lcm(a, b)
    print(f"lcm of {a} and {b} is {c}")