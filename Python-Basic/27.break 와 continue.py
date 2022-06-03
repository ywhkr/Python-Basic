numbers = [5, 15, 6, 20, 7, 25]

for number in numbers: 
    if number < 10:
        continue
    print(number)


#문제 1 
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}


for i in range(len(value_list)):
    character[key_list[i]] = value_list[i]

print(character)


#문제 2 
limit = 10000
i = 1 

sum_value = 0
while sum_value < limit:
    sum_value += i
    i += 1

print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i, limit, sum_value))


#문제 3
max_value = 0
a = 0
b = 0 

for i in range(1, 100):
    j = 100 - i
    print(i, j)
    #최댓값 구하기 
    if max_value < i * j:
        max_value = i * j
        a = i
        b = j 

print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))