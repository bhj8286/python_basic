import random
Fighting_skill = ['boxing', 'judo', 'taekwondo', 'karate']
random_number = random.randint(0,3)
print(Fighting_skill[random_number])

power_level = 149
if 10 <= power_level < 50:
    print('약합니다')
elif 50 <= power_level < 90:
    print('보통입니다')
elif 90 <= power_level < 150:
    print('강합니다')
else:
    print('측정불가입니다')

Top_mc_list = ['강호동', '유재석', '탁재훈']
n = 0
while n < 2:
    print(Top_mc_list[n])
    n = n + 1