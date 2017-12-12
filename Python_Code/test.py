import random

lijst = [22, 23, 24]

test = []

for item in lijst:
    test.append(item)

print(test)

random.shuffle(test)

print(test)
print(lijst)
