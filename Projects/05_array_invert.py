print("행렬의 전치행렬 구하는 프로그램입니다")
ii = int(input("행렬의 행[가로줄] 수를 입력해 주세요 : "))
jj = int(input("행렬의 열[세로줄] 수를 입력해 주세요 : "))
array = [[0]*jj for i in range(ii)]  # 자꾸 까먹는데 반드시 연습할것
array_tmp = [[0]*jj for i in range(ii)]
array_trn = [[0]*ii for i in range(jj)]  # 전치행렬은 A(i,j) -> B(j,i)로 바뀜

print("\n행렬을 입력받겠습니다.")
for i in range(ii):
    for j in range(jj):
        array[i][j] = int(input("%d행 %d열에 들어갈 수 : " % (i+1, j+1)))

print("\n입력한 행렬은 다음과 같습니다.")
for i in range(ii):
    for j in range(jj):
        print("%5d" % array[i][j], end="")
    print()
input("확인:enter")

# 전치행렬을 구함, for문의 i,j순서는 상관없음
for i in range(ii):
    for j in range(jj):
        array_trn[j][i] = array[i][j]
    print()

print("전치행렬은 다음과 같습니다.")  # for문의 i,j순서는 프린트하기위해 j행i열순으로 반복
for j in range(jj):
    for i in range(ii):
        print("%5d" % array_trn[j][i], end="")
    print()
