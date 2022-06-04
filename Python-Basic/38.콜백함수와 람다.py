#콜백함수 
def call_10_times(func):
    for i in range(10):
        func()


def print_hello():
    print("안녕하세요")

call_10_times(print_hello)

# 매개변수 전달

def call_10_times(func):
    for i in range(10):
        func(i)

def print_hello(number):
    print("안녕하세요", number)

call_10_times(print_hello)


#람다 
call_10_times(lambda number: print("안녕하세요", number))



#filter
def 짝수만(number):
    return number % 2 == 0 

a = list(range(100))
b = filter(짝수만, a)
print(list(b))


# 람다 filter
짝수만 = lambda number: number % 2 == 0

a = list(range(100))
b = filter(짝수만, a )
print(list(b))


# map 
def 제곱(number):
    return number * number

a = list(range(100))
print(list(map(제곱, a))) # 기본
print(list(map(lambda number: number * number, a))) #람다버전 
