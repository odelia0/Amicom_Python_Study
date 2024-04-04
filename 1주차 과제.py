import random
number=(int)(random.random()*29)+1
print("%d개"%number)

print("A\nBC\nDEF")

age=random.randint(10,30)
name="kelvin"
print("안녕하세요 제 이름은 %c%s입니다. 제 나이는%d입니다."%(name[0].upper(),name[1:],age))

words=["bird", "rat", "eagle", "cat"]
print(words)
oldWord=input("바꾸고자 하는 단어를 입력하세요: ")
newWord=input("새로운 단어를 입력하세요: ")
oldWordIndex=words.index(oldWord)
words[oldWordIndex]=newWord
print(words)

users={}
userData=input("사용자 정보를 입력해주세요(이름 나이 학년): ")
tmpData=userData.split(" ")
users[tmpData[0]]=[tmpData[1], tmpData[2]]

name=input("조회하고자 하는 사용자 이름을 입력해주세요: ")
print("\n이름: " + name + " 나이: " + users[name][0] + "학년" +
      users[name][1])
