# song = input("너의 최애 노래는?")
# print(song) # 러브 다이브
# print(type(song)) # <class 'str' => "문자열"

# a = input("1 + 1 = ?")
# print(a) # 2
# # "2" 문자열의 타입을 "숫자형(정수형)" 으로 변환 필요
# # => "형 변환환"
# print(a*2) # 22 <= "2" * 2

# 형변환 (type casting, type conversion)
# 1. 정수형으로 변환
print(int("10"), type(int("10"))) # 문자열 "10"을 정수로 변환
print(int(10.9), type(int(10.9))) # 실수 10.9를 정수로 변환 ( 소수점 이하 버림)

# 2. 실수형으로 변환
print(float("11.2"), type(float("11.2"))) # 문자열 "11.2"를 실수로 변환
print(float(10), type(float(10))) # 정수 10을 실수로 변환환

# 3. 형변환 안되는 예시
# print(int("name")) # 숫자 기호가 아닌 문자열을 정수로 변환하려 할 때
# print(int("11.2")) # 실수 문자열을 정수로 변환하려 할 때

b = 2 # 정수형
print(b * 10) # 20
print(str(b) * 10) # 2222222222
print(str(b) + "입니다") # 2입니다
# print(b + "입니다") # type error


# str() 활용 예시
math_score = 80
eng_score = 85
total_scroe = math_score + eng_score
avg_score = total_scroe / 2

print("합계: " + str(total_scroe))
print("평균: " +str(avg_score))
# print("합계: " + total_scroe)
# print("평균: " + avg_score)

# 1번
name = input("이름을 입력하세요.")
age = input("나이를 입력하세요.")
print("안녕하세요!"+ name + "님 (" + age + "세)")

# 2번
name = input("이름을 입력하세요.")
birth = input("태어난 년도를 입력하세요.")
this = input("올해 년도를 입력하세요.") 
age = int(this) - int(birth) + 1
print("올해는" + this + "년", name + "님의 나이는" + str(age) + "세 입니다.")
