array = []

for i in range(0, 20, 2):
    array.append(i * i)

print(array)


#리스트 컴프리헨션 하면
array = [i * i for i in range(0, 20, 2)]
print(array)


#리스트 컴프리헨션 조건문 
array_1 = [i for i in range(10) if i % 3 == 0]



# 1 - 100  / 2진수 / 0이 하나만 포함된 숫자의 합 
output = 0
for i in range(1, 101):
    if "{:b}".format(i).count("0") == 1:
        print("{:b}".format(i)) # 2진수로 변환
        output += i
print("합계: {}".format(output))


# 리스트 컴프리헨션 버전 
output = [i for i in range(1, 101) if "{:b}".format(i).count("0") == 1]
print(output)
print("합계: {}".format(sum(output)))