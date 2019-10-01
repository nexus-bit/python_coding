print("누적합 구하는 알고리즘")
num = int(input("몇 개나 더하시겠습니까? : "))
arr = [0]  # 배열의 첫째 수가 0인 배열 변수 생성
sum = 0
for i in range(0, num):
    arr.append(int(input()))
    # arr[i] = arr.append(int(input())) 아님
    # arr[1]부터 append로 채워짐
    sum += arr[i+1]
    # sum = sum + arr[i+1]
average = sum / num
print("입력한 누적 값은 %d, 평균은 %.2f입니다." %(sum, average))
# 2.f는 소수점 두자리만 출력
