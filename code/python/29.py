# 오버라이딩 : 자식클래스에서 부모클래스의 메서드를 재정의
# i) 부모클래스의 메서드 내용을 자식 클래스에서 완전히 바꿔야할 때
# ii) 부모클래스의 메서드 내용을 그대로로 실행하되, 자식클래스의 메서드에서 추가적인 작업이 더 있을 떄

class Parent:
    def greet(self):
        print("안녕, 부모 클래스")

class Child(Parent):
    def greet(self):
        # super().greet()
        print("안녕, 자식 클래스")

p = Parent()
c = Child()
p.greet()
# 안녕, 부모 클래스
print()
c.greet()
# 안녕, 부모 클래스
# 안녕, 자식 클래스

# 모듈(module)? 여러 기능들이 뭉쳐진 하나의 .py 파일
# 표준모듈(Python에 기본적으로 내장되어 있음)
# 외부모듈(개발자들이 필요에 의해 직접 만든 모듈)

# 만약, 자식클래스에서 추상메서드를 구현하지 못했다면?
# -> 자식클래스에서도 추상메서드로 여전히 남아있음
# -> 그 자식클래스 또한 부모처럼 추상클래스가 됨
# -> 인스턴스 생성 없음

# # 실습 - 상속과 오버라이딩
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     # 재고 업데이트 메서드
#     def updata_quantity(self, amount):
#         self.quantity += amount
#         print(f"{self.name} 재고가 {amount}만큼 {'증가' if amount > 0 else '감소'}했습니다. 현재 재고: {self.quantity}")

#     # 상품 정보 출력 메서드
#     def display_info(self):
#         print(f"상품명: {self.name}")
#         print(f"가격: {self.price}원")
#         print(f"재고: {self.quantity}개")
