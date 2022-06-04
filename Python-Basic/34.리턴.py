def function():
    print("A")
    print("B")
    print("C")
    print("D")
    return # 아무것도 리턴 안하면 none 리턴 

print(function())


#start~end까지 있는 모든 정수를 더하는 함수 
def sum_all(start, end):
    변수 = 0
    for i in range(start, end + 1 ):
        변수 += i
    return 변수 

sum_all(1,100)
sum_all(50,100)


#가변매개변수 곱하는 함수 
def mul(*values):
    변수 = 1
    for i in values:
        변수 *= i
    return 변수
print(mul(5,7,9,10))