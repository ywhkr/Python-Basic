#팩토리얼
n! = 1 * 2 * 3 * ... (n-2 ) * (n-1) * n 

def factorial_1(n):
    변수 = 1 
    for i in range(1, n+1):
        변수 *= i 
    return 변수 

n! = n * (n-1)!
0! = 1 

def factorial_2(n):
    if n == 0:
        return 1
    else:
        return n * factorial_2(n-1)

print(factorial_1(3))
print(factorial_2(3))


# 피보나치 수열 - 메모리제이션 
메모 = {1: 1, 2: 1}
def f(n):
    if n in 메모:
        return 메모[n]
    else:
        output = f(n-1) + f(n-2)
        메모[n] = output
        return output
print(f(150))


# 조기 리턴 
메모 = {1: 1, 2: 1}
def f(n):
    if n in 메모:
        return 메모[n]
    output = f(n-1) + f(n-2)
    메모[n] = output
    return output
print(f(150))
