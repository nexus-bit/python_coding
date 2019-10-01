# 행렬배열을 생성 후 입력받기
arr = [[0, 0, 0],
        [0, 0, 0]]
R = len(arr)  # 행 수
C = len(arr[0])  # 열 수

for i in range(0, R):
    for j in range(0, C):
        arr[i][j] = int(input("%d행 %d열>>" %(i+1, j+1)))
        
print("↓입력한 행렬 출력")
for i in range(0, R):
    for j in range(0, C):
        print(arr[i][j], end = " ")
    print()

 # 배열의 곱셈 만들기
arr1 = [[2, 3],  # i=3행 k=2열
       [4, 7],
       [10, 8]]
arr2 = [[8, 0],  # k=2행 j=2열
       [11, 3]]
arr3 = [[0, 0],  # i=3행 j=2열
       [0, 0],
       [0, 0]]
for k in range(0, 2):
    for j in range(0, 2):
        for i in range(0, 3):
            arr3[i][j] = arr3[i][j] + (arr1[i][k] * arr2[k][j])

print(arr3)



for i in range(20):
    print("ㅎ"*i)
#    1행 1열에는 1행1열*1행1열 + 1행2열*2향1열
 #   1행 2열에는 1행1열*1행2열 + 1행2열*2행2열
  #  2행 1열에는 2행1열*2향1열 + 1행2열*2향1열 ...