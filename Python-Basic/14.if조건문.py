if True: 
    print("True입니다")

if False:
    print("False입니다")


number = input("정수 입력: ")
number = int(number)

if number > 0:
    print("양수입니다")
if number < 0:
    print("음수입니다")
if number == 0:
    print("0입니다")

#오전 오후 구하기
import datetime
now = datetime.datetime.now()

if now.hour < 12:
    print("현재 시간은 {}시로 오전입니다.".format(now.hour))
if now.hour > 12:
    print("현재 시간은 {}시로 오후입니다".format(now.hour))


#홀수와 짝수 
number = int(input("정수 입력: "))

if number % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")
