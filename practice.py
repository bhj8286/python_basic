import random
premier_league_winner = ['Arsenal', 'Mancity', 'Liverpool', 'chelsea']
random_number = random.randint(0,3)
print(premier_league_winner[random_number])

#저장
point_dict = {
    '1위' : 100,
    '2위' : 90,
    '3위' : 80,
}
print(point_dict['1위'])

# 조건 
point = 91
if 80 <= point <= 100:
    print('우승입니다. 축하드립니다.')
elif point >= 70:
    print('준우승입니다')
elif point <= 30:
    print('강등입니다')
else:
    print("잔류입니다")


top_scorer = ['Rooney', 'Henry', 'Ronaldo', 'Gerrad', 'ji-sung Park']
random_number = random.randint(0,4)
print(top_scorer[random_number])
print('득점왕입니다')