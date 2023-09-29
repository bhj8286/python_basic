import random
animals = ['dog', 'cat', 'tiger', 'lion']
random_number = random.randint(0,3)
# print(animals[random_number]) 

back_number = ['10', '7', '4', '9']
# print(back_number)

numbers = range(1, 46)
lucky_number = random.sample(numbers, 6)
print(lucky_number)

numbers = range(1, 46)
lucky_number = random.sample(numbers, 6)
print(sorted(lucky_number))