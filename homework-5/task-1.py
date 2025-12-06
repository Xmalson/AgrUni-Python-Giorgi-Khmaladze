import random
import math

def square_root_(n):
    counter = 0
    for _ in range(n):
        a = random.random()
        b = random.random()
        if math.sqrt(a * a + b * b) <= 1:
            counter += 1
    temp = 4 * counter / n
    print(temp)

square_root_(10)
square_root_(100)
square_root_(10000)
square_root_(1000000)

#yoveli gamodzaxebis shemdeg migebuli pasuxi sul ufro da ufro uaxlovdeba pi-s mnishvnelobas
#imitom rom a da b mnishvnelobebi arian erteulovan kvadratshi
#a^2 + B^2 ki aris erteulovani wrewiri
#am wrewirshi wertilis moxvedris albatoba ki aris pi
