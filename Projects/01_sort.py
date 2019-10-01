print("tset")
arr = [9, 3, 4, 5, 6, 7, 8, 9]  # 파이썬은 배열 종류를 알아서 선언, 또한 arr[1]은 9가아닌 3이 됨
temp = 0
for i in range(1, 7):  # 반복문 조건문은:으로 마침
    for j in range(1, 7):  # 들여쓰기 중요
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
print(arr)

for a in range(1, 7):  # 파이썬은 배열번호0(첫번째)부터 7이전까지 즉 6까지 반복 0,1,2,3,4,5,6
    for b in range(a+1, 8):
        if arr[a] < arr[b]:
            temp = arr[b]
            arr[b] = arr[a]
            arr[a] = temp
print(arr, "\n")


print("오름차순, 내림차순으로 정렬하겠습니다.")
array = []  # 공백 배열 변수 생성
re = int(input("정렬할 숫자는 몇 개입니까 : "))

for i in range(0, re):
    print(i+1, "번째 숫자를 입력하세요 : ", end='')
    # 뒤에 end = ' '를 붙임으로 print이후 줄바꿈X
    array.append(int(input()))
    # arr[0]부터 append로 채워짐
    if array[0] == 0:  # 0을 입력하면 종료하도록 설정
        break

if (array == []) or (array[0] == 0):  # 정렬할 숫자가 없을 때, 취소하고 싶을 때 0을 입력하면 취소됨
    print("프로그램을 종료합니다")
else:
    print("입력된 배열은", array, "입니다")
    for i in range(0, re-1):
        for j in range(i+1, re):
            if array[i] > array[j]:
                    temp = array[i]
                    array[i] = array[j]
                    array[j] = temp
    print("셀렉션 솔트 오름차순으로 정렬된 배열은", array, "입니다.")

    for i in range(0, re-1):
        for j in range(0, re-1):
            if array[j] < array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    print("버  블 솔트 내림차순으로 정렬된 배열은", array, "입니다.")
