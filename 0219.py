# import turtle
# n = 20
# count = 0 # 초기값
# # if num>0:
# #     print('hello nomad')
# # elif num <0:
# #     print('한글')
# # else:
# #     print('zero')
# while count <n: # 루프 조건
#     turtle.forward(100)
#     turtle.right(360/n)
#     # print('run', count)
#     count = count + 1 # 조건의 변화
# y = 0

# while y < 200:
#     x = 0
#     while x < 200:
#         turtle.up()
#         turtle.goto(x, y)
#         turtle.down()
#         turtle.dot(3)
#         x = x + 20 
#     y = y + 20

# """ menu = """ 1. 학생추가
#     2. 학생 삭제
#     3. 학생 목록 보기
#     4. 종료 """
# number = 0
# while number != 4:
#     print(menu)
#     number = int(input('메뉴 번호를 입력하세요: '))
#     if number in [1, 2, 3, 4]:
#         print('{}번 메뉴를 선택했습니다.\n'.format(number))
#     else:
#         print('{}번 없는 메뉴를 선택했습니다.\n'.format(number))
# else:
#     print('bye') """

# fruits = ['사과', '딸기', '바나나', '블루베리', '포도', '우유']
# for fruit in enumerate(fruits):
#     print(fruit)
# print((3>0) and (3<5))
# print((3>0) & (3<5))
# print((3>0) | (3<5))
# from random import *
# print(random())
# print(int(random()*10))
# print(int(random() * 46) + 1)
# print(randint(1,45))
# jumin = '111230-20306621'
# print('성별: ' +jumin[7])
# print('년: ' +jumin[:2])
# print('월: ' +jumin[2:4])
# print('나는 %d살 입니다.' % 18)
# print('나는 %s을 좋와합니다.' % '파이선')
# print('파이선은  %c로 시작합니다.' % 'P')
# print('나는 %s과 %s을 좋와합니다.' %('컴공', '인공지능'))
# print('나는 {}살입니다.'.format(18))
# print('나는 {}과 {}을 좋와합니다.'.format('컴공', '인공지능'))
# print('나는 {0}과 {1}을 좋와합니다.'.format('컴공', '인공지능'))
# print('나는 {1}과 {0}을 좋와합니다.'.format('컴공', '인공지능'))
# print('나는 {소속}이며 {지능}과목을 좋와합니다.'.format(소속='컴공', 지능='인공지능'))
# age = 18
# dep = '인공지능'
# print(f'나는 {age}입니다. 세명컴퓨터고등학교 {dep}과 학생입니다.')
# \n 줄바꿈 탈출문자
# print(f'나는 18입니다.\n 세명컴퓨터고등학교 인공지능과 학생입니다.')
# print('나는 18입니다.\"세명컴퓨터고등학교 인공지능과\" 학생입니다.')
# print('C:\\Users\\nomad\\anaconda3')
# \b 한글자 삭제
# print('computerr\bAI')
#  \t :탭
# print('computerr\tAI')

# 리스트
# bus = ['서울', '인천', '대구', '대전', '수원']
# print(bus)
# # 인천은 먗 번 째인가?
# print(bus.index('인천'))
# # 안양을 추가
# bus.append('안양')
# print(bus)
# # print(bus.pop())
# print(bus)
# # 같은 도시가 몇개인지
# bus.append('안양')
# print(bus.count('안양'))

# # 정렬하기
# no = [ 2,37, 45, 9, 10, 1, 0, 39]
# no.sort()
# print(no)
# # 역순으로 정렬하기
# no.reverse()
# print(no)

# # 모두 지우기
# no.clear()
# print(no)

# # 다양한 자료형과 함께 사용
# con = ['세명', 16, False, True]
# print(con)
# # 리스트 확장
# con_1 = [ 34, 56, 78, 12]
# con.extend(con_1)
# print(con)

# 사전
# stu = {3: '세명', 6:'인공', 9:'컴퓨터'}
# print(stu[3])
# print(stu.get(9))
# print(stu.get(8)) # 답이 없음
# print(stu.get(8, '지능')) # 8에 지능을 생성
# print(7 in stu) # False
# print(6 in stu) # True

# stu = {'은평-3': '세명', '가좌-6':'인공', '홍재-9':'컴퓨터'}
# print(stu['가좌-6'])
# # 딕셔너리 추가
# stu['1학년'] = '고등학생' #추가
# stu['가좌-6'] = '전입생' # 업데이트
# print(stu)
# del stu['은평-3'] # 키 삭제
# print(stu)
# print(stu.keys()) # 키만 출력
# print(stu.values()) # 밸류만 출력
# print(stu.items()) # 키 밸류 쌍으로 출력

# 함수는 재사용할 수 있는 명령문 묶음
# # 매개변수가 없는 함수
# def say():
#     print('안녕!!!')
# say()

# # 매개변수가 있는 함수
# def say(nomad):       # nomad는 매개변수이다
#     print('안녕!!!', nomad) # nomad는 매개변수이다
# say("good!") # # good!는 매개변수이다

# klist = ('a', 'c', 'd', 'f', 'h')
# x = len(klist)
# print(x)

# 재귀함수는 계승함수

# def plus(n):
#     if n == 0:  # 만약 n이 0이면
#         return 0 # 0을 반환한다.
#     else:        # 만약 n이 0이 아니면
#         return n + plus(n-1)
# print(plus(5))



