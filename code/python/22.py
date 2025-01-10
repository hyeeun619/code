# 클래스 변수와 인스턴스 변수

# 클래스 변수 : "클래스에 속한" 변수 -> 모든 인스턴스(객체)가 공유하는 변수
# 인스턴스 변수 : "각각의 인스턴스에 속한" 변수 -> 각 인스턴스(객체)가 독립적으로 관리하는 변수

class Dog:
    kind = "진돗개" # 클래스 변수

    # 생성자자
    def __init__(self, name):
        self.name = name # 인스턴스 변수

# 클래스(설계도)로부터 인스턴스(객체)를 생성
dog1 = Dog("백구")
dog2 = Dog("초코")

# 인스턴스 변수 접근
print(dog1.name)
print(dog2.name)

# 클래스 변수 접근
# i) 인스턴스 변수를 통해 접근
print(dog1.kind)
print(dog2.kind)
# ii) 클래스명을 통해 접근
print(Dog.kind)