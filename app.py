import imp
import numbers
import random
import string

print(random.random())
print(random.randint(2, 20))

print(random.random())
print(random.randint(1, 20))
print(random.choice([1, 2, 3, 4]))
print(random.choices([1, 2, 3, 4], k=2))
print("".join(random.choices("string.ascii_letters + string.digits", k=8)))

numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)
