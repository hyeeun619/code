# while 문
i = 0
while i > 0:
    print("반복문 연습", i)
    i -= 1
print("종료")

# 합계 구하기
num = 1 # 더하는 숫자
total = 0 # 총합
while num <= 10:
    total += num # total = total + num
    print("현재 total 값 >", total)
    num += 1 # num = num + 1

print(f"1부터 10까지의 합은 {total}입니다.")

# 입력값 받기
user_input = ""
while user_input != "종료":
    user_input = input("원하는 값을 입력하세요. '종료' 입력시 종료됩니다.")
    print(f"입력한 값: {user_input}")

print("프로그램이 종료되었습니다.")

# break 문
# 예시. 숫자를 입력받아서 0이 입력되면 반복문 종료
while True:
    num = int(input("숫자입력 (0 입력시 종료):"))
    
    if num == 0:
        print("프로그램 종료")
        break

    print(f"입력한 숫자는 {num}입니다.")

# continue 문
# 예시. 숫자 입력받고 짝수만 출력하고 홀수는 건너뛰기
while True:
    num = int(input("숫자 입력 (음수 입력시 종료):"))
    
    if num < 0:
        print("프로그램 종료")
        break # 음수 입력시 프로그램 종료료

    if num % 2 != 0:
        continue # 홀수는 건너뛰고, 다시 입력 받기

    print(f"입력한 짝수는 {num}입니다.")


# 실습 1
while True:
    hye = input("양수를 입력하세요. ('종료' 입력시 프로그램 종료):")

    # hye 변수 값이 "종료" 문자열과 값이 같다면
    if hye == "종료":
        print("프로그램을 종료합니다.")
        # 프로그램 종료 (반복문을 빠져나와야 함)
        break

    # hye 변수 값이 "0" 이라면
    if hye == "0":
        # 이번 반복 회차는 건너뛰고, 다음 반복회차로 계속 나아감
        continue

    num = 1
    total = 0
    # num(1)부터 hye(사용자가 입력한 값)까지의 total(총합)
    while num <= int(hye):
        total += num
        num += 1
    print(f"1부터 {hye}까지의 합은 {total}입니다.")

    if hye < "0":
        print("양수만 입력 하세요.")


# 실습1 다른방법
while True:
    positive_input = input("양수를 입력하세여 ('종료' 입력시 프로그램 종료): ")
    
    if positive_input == "종료":
        print("프로그램을 종료 합니다")
        break
    
    try: 
        positive_input = int(positive_input)
        
        if positive_input < 0:
            print("양수만 입력하세여")
            continue
        elif positive_input == 0:
            continue
        else:
            result = 0
            i = 1
            
            while i <= positive_input:
                result = result + i
                i = i + 1
                
            print(f"1부터 {positive_input}의 합은 {result}입니다")

    
    except:
        print("양수만 입력하세여")
        continue


# 실습 1 다른 방법
while True:
    user_input = input("양수를 입력하세요.('종료'입력시 프로그램 종료): ")

    if user_input == "종료":
        print("프로그램을 종료합니다")
        break

    if not user_input.isdigit():  # True -> not False
        print("양수를 입력하세요")
        continue

    number = int(user_input)
    if number == 0:
        continue

    total = 0
    num = 1
    while num <= number:
        total += num
        num += 1
    print(f"1부터 {number}까지의 합은 {total}입니다.")
