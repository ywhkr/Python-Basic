#리스트 함수 : min(), max(), sum()
min([273,23,123,52])
max([273,23,123,52])
sum([262,142,123,1])


#reversed() 리스트 뒤집기 - 일회용 함수 
a = [0, 1, ,2, 3, 4, 5, 6]
reversed_a = reversed(a)
print(list(reversed_a))

# reversed 반복문 
for i in reversed(리스트): 

##enumerate() 현재 인덱스가 몇 번째 인지 확인하기 - 일회용 함수 
a = [273, 103, 52, 32, 57]
for i, element in enumerate(a):
    print("{}번째 요소는 {}입니다.").format(i, element)



#items() 딕셔너리로 쉽게 반복문 작성 - 일회용 함수  

a = {"key_1: "value_1", "key_2 : "value_2", "key_3: "value_3"}
for key, value in a.items():
    print("{}키의 값은 {}입니다.").format(key,value)

    