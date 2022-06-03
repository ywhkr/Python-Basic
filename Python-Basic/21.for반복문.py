from doctest import OutputChecker


a = [1,2,3,4,5,6,7]

for element in a:
    print(element)

=> 1,2,3,4,5,6,7



# 조건문,반복문 혼합 
numbers = [273, 103, 5 ,32 ,65, 9, 72, 800, 99]

for number in numbers: 
    if number >= 100:
        print("- 100이상의 수: {}".format(number))


#반복문 중첩 
list_of_list = [
    [1,2,3],
    [4,5,6,7],
    [8,9]
]

for a in list_of_list:
    for b in a:
        print(b)


numbers = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]

for number in numbers:
    output[(number-1) % 3].append(number)

print(output)