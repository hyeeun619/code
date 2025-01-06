# 튜플, Tuple
t1 = (1,) # 요소가 1개인 튜플은 반드시 쉼표 사용!
print(t1)

not_tuple = (1)
print(not_tuple) # 정수

t2 = (1, 2, 3, 4, 5, 3, 3, 3) # 괄호를 사용해 튜플 선언
print(t2)

t3 = 1, 2, 3 # 괄호 없이 쉼표만 사용 튜플 선언 가능능
print(t3)

t4 = ("a", "b", "c", ("안녕", "감자"))
print(t4) 

print(t1[0])
print(t2.count(3))
print(t3.index(2))
print(t4[3][0])
print(t4[:2])

print("a" in t4)
print("d" in t4)

# t4[0] = "x"
