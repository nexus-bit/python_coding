# 가우스 소거법 → https://thrillfighter.tistory.com/198 절대못해
# ★☆유튜브 가우스☆★ → https://www.youtube.com/watch?v=mpTjc893sjI
# 2x2역행렬 → https://terms.naver.com/entry.nhn?docId=3350377&cid=60210&categoryId=60210
# 분수 출력방법 → https://blog.naver.com/okkam76/221259612857
# 검토하는곳 → https://matrix.reshish.com/inverCalculation.php
num = int(input("역행렬을 구하는 프로그램입니다.\n2X2행렬은 1번\n3x3행렬은 2번\n└→ "))
if num == 1:
    arr = [[0]*2 for i in range(2)]  # →2x2행렬 선언
    arr_tmp = [[0]*2 for i in range(2)]  # →2x2행렬 선언 --
    for i in range(2):  # ┌2x2행렬 입력 -------------------
        for j in range(2):
            arr[i][j] = int(input("%d행 %d열>>" % (i+1, j+1)))
    # ┌입력한 2x2행렬 출력 -------------------
    print("→입력값\n┌---------┐")
    for i in range(2):
        for j in range(2):
            print("%4d" % arr[i][j], end="")
        print("")
    input("└---------┘\n입력값 확인:enter")

    yuinza = arr[0][0]*arr[1][1] - arr[0][1]*arr[1][0]
    if yuinza == 0:  # →ad-bc(여인자)의 값이 0이면 역행렬X --------
        print("여인자 값이 0이기 때문에 역행렬을 구할 수 없습니다.")
    else:
        arr_tmp[0][0] = arr[1][1]
        arr_tmp[0][1] = arr[0][1] * -1
        arr_tmp[1][0] = arr[1][0] * -1
        arr_tmp[1][1] = arr[0][0]
        # ┌여인자를 계산(곱함)과 동시에 출력
        from fractions import Fraction
        # └내장 라이브러리의 fraction모듈 사용, Fraction클래스 읽기(분수로 출력하기 위함)
        print("→계산 결과\n┌-----------┐")
        for i in range(2):
            for j in range(2):
                arr[i][j] = Fraction(arr_tmp[i][j], yuinza)
                # └왜인지는 모르나, arr_tmp[i][j] / yuinza로 입력하면 에러발생
                print("%6s" % arr[i][j], end="")
            print("")
        print("└-----------┘")
        print("프로그램을 종료합니다\n", arr)  # 이상하게도 이렇게 직접 출력하면 분수fraction그대로 나옴

elif num == 2:
    arr = [[0]*3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            arr[i][j] = int(input("%d행 %d열>>" % (i+1, j+1)))
    print("여인자+가우스 소거법 배운 뒤에 다시 찾아뵙겠습니다.")

else:
    print("프로그램이 장난이냐")
