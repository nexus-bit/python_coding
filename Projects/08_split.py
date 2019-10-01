a, b, c = input("숫자 세 개 입력>>").split()  # 공백으로 분리해서 동시에 변수 입력
add = int(a) + int(b) + int(c)
# average = (a + b + c)/3  # 에러 발생 : 입력받은 문자열은 나눌 수 없음
average = add/3
print("합은 %d, 평균은 %.2f" %(add, average))
# 멍청하게 print("합은 %d, 평균은 %.2f" %add %average) 하지 말자고
