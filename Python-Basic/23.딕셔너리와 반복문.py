

딕셔너리 = {
    "키A": "값A"
    "키B": "값B"
    "키C": "값C"
}

딕셔너리["키A"] => "값A"
딕셔너리["키B"] => "값B"
딕셔너리["키C"] => "값C"

#2 

딕셔너리 = {
    "문자열" : "값"
    273: [1,2,3,4]
    True: False
}

print(딕셔너리["문자열"])
print(딕셔너리[273])
print(딕셔너리[True])

# 반복문과 조합 
for key in 딕셔너리: 
    print("{} : {}".format(key, 딕셔너리[key])


# 요소 추가 
딕셔너리["키"] = "값"

# 요소 제거 
del 딕셔너리["키"]


#get 
print(딕셔너리.get("이름")) == print(딕셔너리["이름"])

없는 값을 get하면 none 이 나옴 




# counter 코드 
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1
print(counter)


# flat
character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is dict:
        for k in character[key]:
            print("{} : {}".format(k, character[key][k]))
    elif type(character[key]) is list:
        for item in character[key]:
            print("{} : {}".format(key,item))
    else:
        print("{} : {}".format(key, character[key]))