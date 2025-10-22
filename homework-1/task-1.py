a = float(input("Enter first side of triangle: "))
b = float(input("Enter second side of triangle: "))
c = float(input("Enter third side of triangle: "))

#pirobashi ar ewera, magram davamate samkutxedis shemowmebis nawilic realuri rom yofiliyo

if a + b > c and a + c > b and b + c > a:
    perimeter = a+b+c
    p = perimeter/2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(perimeter)
    print(area)
else:
    print("The given sides are not valid for triangle")