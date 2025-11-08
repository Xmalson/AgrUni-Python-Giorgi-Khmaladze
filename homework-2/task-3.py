import random
tempcounter = 0
number_list = []
while tempcounter < 5:
    number_list.append(random.randint(1, 4))
    tempcounter += 1

print(number_list)

final_list = []

for i in number_list:
    final_list.extend([i]*i)
print(final_list)
print(len(final_list))

