def print_n_times(value, n):
    for i in range(n):
        print(value)


print_n_times("안녕하세요", 5)


#가변 매개변수 함수 
def 함수이름(매개변수1, 매개변수2, *가변매개변수):
    print(매개변수1)
    print(매개변수2)
    print(가변매개변수)
    

함수이름(0,1,2,3,4,5,6,7,8,9)

- 가변매개변수는 함수에 하나만 허용
- 가변매개변수는 앞에 적을 수 없다


# 기본 매개변수 
def print_n_times(value, n=5):
    for i in range(n):
        print(value)


print_n_times("안녕하세요")


- 기본 매개변수는 마지막에 입력한다. 


# 가변 매개변수, 기본 매개변수 혼합
def function(일반매개변수1,일반매개변수2, *가변매개변수, 기본매개변수 = 10)
    print(일반매개변수1,일반매개변수2)
    print(가변매개변수)
    print(기본매개변수)
  
function(0,1,2,3,4,5,6,7,7,8,9,12,151,기본매개변수 = 15) 