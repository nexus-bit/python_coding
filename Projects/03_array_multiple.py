# https://daeqws4.blog.me/221378519527
# https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=1040101&docId=238278007&qb=7ZaJ66CsIOyeheugpeuwm+q4sA==&enc=utf8&section=kin&rank=2&search_sort=0&spq=0&pid=UbIpwdpySEsssvXq7PwssssstDs-493251&sid=H%2BDFDRMeg5/CUT5R50SRnf5F

print("\n※이번 시간에는 배열의 곱셈을 만들어 볼 거에요※\n")  # 주의:행렬에서 A*B =! B*A임을 명심

ii = int(input("첫번째 행렬의 행(i) 수를 입력하세요>>"))
kk = int(input("첫번째 행렬의 열(k) 수를 입력하세요>>"))
jj = int(input("두번째 행렬의 열(j) 수를 입력하세요>>"))

arr1 = [[0]*(kk) for i in range(ii)]  # arr1은 ii행*kk열의 사이즈로 0으로 채워진 MATRIX
arr2 = [[0]*(jj) for i in range(kk)]  # arr2는 kk행*jj열의 사이즈로 0으로 채워진 MATRIX
arr_result = [[0]*(jj) for i in range(ii)]  # 행렬 곱셈의 결과는 ii행 jj열이다.

print("\n곱셈의 결과는 %dx%d행렬입니다" % (ii, jj))

print("\n첫 번째 행렬에 대해 조사받겠습니다.")  # arr2 입력반복문
for i in range(0, ii):
    for k in range(0, kk):
        arr1[i][k] = int(input("%d행 %d열>" %(i+1, k+1)))  # 파이썬은 0행0열부터라서 +1

print("\n입력받은 첫 번째 행렬입니다.")  # arr1 출력반복문, 위에다 합치면 안됨..
for i in range(0, ii):
    for k in range(0, kk):
        print("%3d" %(arr1[i][k]), end = " ")  # %3d로 두자리 수일때 밀림 방지, end구분은 스페이스
    print("")  # 행 표시후 다음 열에 행 표시하기 위한 <enter>

print("\n두 번째 행렬에 대해 조사받겠습니다.")
for k in range(0, kk):
    for j in range(0, jj):
        arr2[k][j] = int(input("%d행 %d열>" %(k+1, j+1)))

print("\n입력받은 두 번째 행렬입니다.")
for k in range(0, kk):
    for j in range(0, jj):
        print("%3d" %(arr2[k][j]), end = " ")
    print("")

print("\n※행렬의 곱셈 결과는 다음과 같습니다.※")
for k in range(0, kk):
    for j in range(0, jj):
        for i in range(0, ii):
            arr_result[i][j] = arr_result[i][j] + arr1[i][k] * arr2[k][j]

for i in range(0, ii):  # 출력 반복문은 어쩔 수 없이 따로 만들어야함
    for j in range(0, jj): 
        print("%5d" %arr_result[i][j], end="")  # 깰끔!하게 출력하기 위해 %5d를 썼다
    print("")
