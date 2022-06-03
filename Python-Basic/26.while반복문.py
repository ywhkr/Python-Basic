import numbers


while <불 표현식>:
    내용 - (반복 실행)


while True:
    print(".", end= " ")
    


# 예제 
numbers = [1,2,1,2,1,2,1,2]

while 1 in numbers:
    numbers.remove(1)
    print(numbers)


# 예제 2 ( 5초 대기 후 프로그램 실행 )
import time 
처음 = time.time()
while 처음 + 5 >= time.time():
    pass
print("프로그램이 종료되었습니다")
