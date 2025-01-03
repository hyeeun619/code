# 한 줄 주석 (ctrl+/)
# Python 파일 실행 단축기: ctrl + F5

'''
여기는
여러줄
주석입니다
'''

"""
쌍따움표 세개도
여러줄
주석입니다
"""

print("Hello World")
print("Hello", "World")
print("Hello", "World", sep="") # seperate, 구분자자
print("010", "1234", "4321", sep="-") # 공백에 - 표시 
print("Hello", "Python", 1, 2, sep="_") # 자료형 달라도 됨
print() # print 함수 안에 아무것도 안넣으면 줄바꿈 처리 됨됨
print("1111")
print("안녕하세요, ", end="") # end 옵션 : 문장 끝에 넣고 싶은 것
print("코딩온입니다.")
print("안녕하세요 ", end=", ") # 결과 동일일
print("코딩온입니다.")

ive = "I AM"
print(ive)
ive = "장원영"
print(ive)
print(f"제가 좋아하는 가수는 {ive}입니다.") # f 문자열 포매팅
print("제가 좋아하는 가수는 ", ive, "입니다.", sep="") # 위와 결과 동일
