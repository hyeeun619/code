# 딕셔너리 (dictionary)

# 생성
# dict1 = {}
dict1 = dict()
print(dict1)

# 딕셔너리 생성
dict1 = {"name" : "홍길동", "age" : 20, "city" : "Seoul", "hobby" : ["런닝", "등산", "헬스"]}
print(dict1)

dict2 = dict(name = "홍길동", age = "21")
print(dict2)

# 값 접근하기
print(dict1["name"])
print(dict1["hobby"])
print(dict1["hobby"][2])

# 값 수정
dict1["age"] = 30
print(dict1)

# 요소 추가
dict1["birthday"] = ["19900101"]
print(dict1)

# 키 삭제
del dict1["birthday"]
print(dict1)

# 딕셔너리 메서드
fruits = {"apple" : "사과", "banana" : "바나나"}
print(fruits.get("apple"))
print(fruits.get("peach"))
# -> 존재하지 않는 키로 get 하는 경우 'None' 반환
print(fruits.get("peach", "복숭아"))
# -> 존재하지 않는 키로 검색시 기본값 설정
print(fruits)
# -> 기본값을 설정할 뿐, 딕셔너리 요소 추가 x

# 여러 요소 추가
fruits.update({"grapes" : "포도", "melon" : "멜론"})
print(fruits)
# print(fruits.key())
print(fruits.values())
print(fruits.items())

# 요소 모두 지우기
fruits.clear()
print(fruits)

# 실습
# 1번
student = {}
# 2번
student = {"Alice" : 85, "Bob" : 90, "Charlie" : 95}
print(student)

# 3번
student["David"] = 80
print(student)

# 4번
student["Alice"] = 88
print(student)

# 5번
del student["Bob"]
print(student)

