a = int(10)
b = int(3)
print("나눈 것은 %lf, 몫은 %d, 나머지는%d" %(a/b, int(a/b), a%b))
print("나눈 것은", a/b, "몫은", int(a/b), "나머지는", a%b)  # int(수)로 정수만 뽑을 수 있음
print()

print("약수를 구해드려요")
number01 = int(input("첫번째 수>>"))
number02 = int(input("두번째 수>>"))
arr01 = []
arr02 = []
arr_r = []
for i in range(1, number01+1):
    if int(number01 / i) == (number01 / i):
        arr01.append(i)
print(number01, "의 약수는", arr01)

for i in range(1, number02+1):
    if int(number02 / i) == (number02 / i):
        arr02.append(i)
print(number02, "의 약수는", arr02)

for i in range(0, len(arr01)):  # len으로 배열의 크기 확인 가능
    for j in range(0, len(arr02)):  # 배열의 크기만 루프 돌려서 겹치는 수가 곧 공약수
        if arr01[i] == arr02[j]:
            arr_r.append(arr01[i])
print("공약수는", arr_r)
print("최대공약수는", arr_r.pop())  # arr_r.pop() 을 쓰면 배열의 마지막 수를 꺼내온다.
print("최대공약수를 제외한 공약수는", arr_r)
