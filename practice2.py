import random
singer_list = ['BIGBANG', 'BTS', '2PM', 'BLACKPINK', 'TWICE']
random_number = random.randint(0,4)
print(singer_list[random_number])

debut_dict = {
    '빅뱅' : 2006,
    '투피엠' : 2008,
    '트와이스' : 2015,
}
print(debut_dict['빅뱅'])

point = 100

if 90 <= point <= 100:
    print('대상입니다.')
elif 80 <= point < 90:
    print('우수상입니다.')
elif 70 <= point < 80:
    print('장려상입니다.')
else:
    print('아쉽습니다.')

BIGBANG_MEMBER_LIST = ['GD', 'TAEYANG', 'DAESUNG', 'T.O.P']
print('빅뱅멤버')
n = 0
while n < 4:
    print(BIGBANG_MEMBER_LIST[n])
    n = n + 1

