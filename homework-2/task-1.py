while True:
    n = input("please enter an year: ")
    if not n.isdigit() or int(n) <= 0:
        print("please enter a valid year")
        continue

    n = int(n)


    if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
        print("it is a leap year")
    else:
        print("it is NOT a leap year")
    break