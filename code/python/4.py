#리스트
number = [1, 2, 3, "Hello","Pyhton"]
print(number) # [1, 2, 3, 'Hello', 'Pyhton']

# 인덱싱 (Indexing) : 인덱스 번호로 요소를 추출하는 행위
print(number[3]) # Hello
print(number[0]) # 1
# print(number[100]) # IndexError: list index out of range (인덱스 범위 벗어남)

# list() 함수수 : 리스트를 생성하는 내장함수 (반복 가능한 객체를 리스트로 변활할 때 사용)
#  반복 가능한 객체? (ex. 문자열, 튜플, 셋(집합), 딕셔너리, 또 다른 리스트)
text = "Hello, Python"
print(list(text)) # ['H', 'e', 'l', 'l', 'o', ',', ' ', 'P', 'y', 't', 'h', 'o', 'n']

# invalid = 1234
# print(list(invalid)) 
# # TypeError: 'int' object is not iterable (정수는 반복 가능한 객체가 아님)

# 참고. 문자열의 인덱싱과 슬라이싱
print(text[7]) # P
print(text[7] + text[8] + text[9] + text [10] + text[11] + text[12]) # Python
print(text[7:]) # Python

#  퀴즈. 문자열 슬라이싱
date = "20250106"
year = date[0:4] # index 0~3
month = date[4:6] # index 4~5
day = date[6:] # index 6~7
print(year + "년" + month + "월" + day + "일") # 2025년01월06일

#문자열에서 사용 가능한 함수
print(len(date)) # len() : 문자열의 길이를 구하는 함수
print(len(text))
print(text.count("p")) # count() : 문자열 내에서 특정 부분 문자열이 등장한 횟수 구하는 함수 (대소문자 구별)

# 리스트 인덱싱과 슬라이싱
shop = ["반팔", "청바지", "이어폰", ["무선키보드", "기계식키보드"]]
print(shop[:2]) # 0 <= shop < 2
print(shop[3]) 
print(shop[-2]) # 음수 인덱싱 가능 (뒤에서부터 카운팅, -1부터 시작)
print(shop[:]) # 처음부터 끝까지

# 리스트 수정
shop[0] = "긴팔"
print(shop)
print(shop[1]) # 청바지
# shop[100] = "신발"
# print(shop) # IndexError: list assignment index out of range

# 리스트 삭제
del shop[1] # 단일 삭제
print(shop)
print(shop[1]) # 이어폰

del shop[2:] # 복수 삭제
print(shop)

# 리스트 연산
a = [1, 2, 3]
b = ["안녕", "반가워"]
print(a + b) # 이어쓰기
print(b * 3) # 반복하기

# 정렬 함수
# asc : ascending (오름차순)
# desc : descending (내림차순)
num = [3, 1, 5, 2]
num_asc = sorted(num)
print(num)
print(num_asc)

num_desc = sorted(num, reverse = True)
print(num_desc)

num.sort() # 매서드
print(num)

korean = ["강", "이", "박", "최", "김"]
korean.sort(reverse=True)
print(korean)

alphabet = ["b", "c", "a", "d"]
alphabet.reverse() # 내림차순이 아니라 인덱스 역순
# -> 새로운 리스트 반환하지 않고 원본 리스트를 변경
print(alphabet) 

print(alphabet.index("c")) # 2

#  요소 추가/삭제/삽입
a = ["a", "b", "c", "안녕", "hi"]
print(a)

a.append("Good")
print(a)

a.pop()
print(a)

a.pop(2)
print(a)

a.remove("안녕")
print(a)

a.insert(2, "잘가")
print(a)

a.clear()
print(a)

x = ["q", "w", "e", "r", "w"]
print(x.count("w"))

# 실습 문제
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', ' indigo', 'purple']

# 2번 인덱스 값 출력
print(rainbow[2])

# 알파벳 순서로 정렬한 값 출력
rainbow.sort()
print(rainbow)

sorted_rainbow = sorted(rainbow)
print(sorted_rainbow)

# 좋아하는 색 맨 마지막에 추가하기
rainbow.append("pink")
print(rainbow)

# 3~6번째 값 삭제하기
del rainbow[3:7] # 복수 삭제
print(rainbow)

