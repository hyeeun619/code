# # 이중 for문
# for i in range(5):
#     print(f"외부 반복문의 i값: {i}")

#     for j in range(3):
#         print(f"내부 반복문의 j값: {j}")
        
#     print("------------")

# 이차원 리스트와 이중 for문
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 요소 (elem 변수)의 합계 구하기
total_sum = 0
for row in matrix:
    # print(f"외부반복문의 row: {row}")

    for elem in row:
        # print(f"내부반복문의 elem: {elem}")
        total_sum += elem
    # 1번 시점 : 내부 반복문이 종료될 때
    print(f"중간 합계: {total_sum}")
# 2번 시점 : 외부 반복문이 종료될 때
print(f"전체 합계: {total_sum}")

# 짝수만 출력하기
matrix2 = [
    [4, 21, 77],
    [60, 17, 98],
    [2, 74, 33]
]
print("짝수만 출력:", end=" ")
for row in matrix2:
    for elem in row:
        if elem % 2 == 0:
            print(elem, end = " ")
print()

# 실습 1
for i in range(2,10):
    print(f"{i}단")
    for j in range(1,10):
        print(f"{i}x{j}={i*j}")

# 실습 2
for i in range(3): # 가로 반복
    for j in range(5): # 세로 반복복
        print("*", end = "")
    print()

# 실습 3
for i in range(4):
    for j in range(1+i):
        print("*", end = "")
    print()

# 실습 4
for i in range(5):
    for j in range(5-i):
        print("*", end = "")
    print()

# 실습 5 ??
for i in range(4):
    for j in range(7):
        print("*", end = "")
    print()