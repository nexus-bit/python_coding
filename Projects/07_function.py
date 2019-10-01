# 참고 http://engineerk.com/221237374300
# 문자열의 함수 활용--------------------


def order(a, b):
    print(a, b, "파스타 주문하셨나요?")


order("봉골레", "까르보나라")
# 문자열과 숫자의 합--------------------


def plus(a, b):
    """
    →tip:큰따옴표 주석 사용할 때는 들여쓰기 해야 함
    """
    print(a + b)


plus(7, 4)
plus("노준수", "유학생")
# 반환값이 있는 경우--------------------


def mult(a, b):
    c = a * b
    return(c)


print(mult(2, 6))
# 처음에 착각한 내용--------------------
'''
안좋은 예① : 반환값이 없는 경우
def mult(a, b):
    a * b
print(mult(3,4))
안좋은 예② : 함수 내의 인자를 직접 사용한 경우
def mult(a, b):
    c = a * b
    return(c)
print(c)
'''
# 반환값이 두 개인 경우-----------------


def ABC(var1, var2=0):
    a, b = var1, var2
    # do something
    return a, b


res1, res2 = ABC(10, 3)
print(res1 + res2)
# 함수 내의 조건, 문자로 반환------------


def divide(var1, var2):
    if var2 == 0:
        return "Err : 0으로 나눌 수 없습니다"
    else:
        res = var1 / var2
        return res


print(divide(28, 2))
print(divide(3, 0))
# 최대 자릿수를 검사하기 위한 함수--------


def check(var):
    str_var = str(var)  # 숫자를 문자로 변환하는 내장함수
    if len(str_var) > 3:  # 문자의 길이를 알아내는 내장함수(숫자X)
        return('Error : Length Limits')
    else:
        return var


print(check(123))
print(check(1234))
