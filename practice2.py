# import random
# singer_list = ['BIGBANG', 'BTS', '2PM', 'BLACKPINK', 'TWICE']
# random_number = random.randint(0,4)
# print(singer_list[random_number])

# debut_dict = {
#     '빅뱅' : 2006,
#     '투피엠' : 2008,
#     '트와이스' : 2015,
# }
# print(debut_dict['빅뱅'])

# point = 100

# if 90 <= point <= 100:
#     print('대상입니다.')
# elif 80 <= point < 90:
#     print('우수상입니다.')
# elif 70 <= point < 80:
#     print('장려상입니다.')
# else:
#     print('아쉽습니다.')

# BIGBANG_MEMBER_LIST = ['GD', 'TAEYANG', 'DAESUNG', 'T.O.P']
# print('빅뱅멤버')
# n = 0
# while n < 4:
#     print(BIGBANG_MEMBER_LIST[n])
#     n = n + 1

def solution(n):
    
    numbers = list(range(0, n+1))
    answer = 0
    for number in numbers:
        if number % 2 == 0:
            answer += number
    return answer
print(solution(10))

def solution(angle):
    if 0 < angle < 90:
       return 1
    elif angle == 90:
       return 2
    elif 90 < angle < 180:
        return 3
    elif angle == 180:
        return 4
print(solution(95))


print(sum(range(0, 11, 2)))

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)


menus = ['라면', '김밥', '떡볶이', '돈가스', '만두']
for index, menu in enumerate(menus):
    print(index, ':', menu, sep='')