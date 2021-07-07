'''
문제 설명

다음을 만족하는 함수, solution을 완성해주세요.

solution 함수는 이차원 리스트, mylist를 인자로 받습니다
solution 함수는 mylist 원소의 행과 열을 뒤집은 한 값을 리턴해야합니다.
예를 들어 mylist [[1, 2, 3], [4, 5, 6], [7, 8, 9]]가 주어진 경우, solution 함수는 [[1, 4, 7], [2, 5, 8], [3, 6, 9]] 을 리턴하면 됩니다.

제한 조건
mylist의 원소의 길이는 모두 같습니다.
mylist의 길이는 mylist[0]의 길이와 같습니다.
각 리스트의 길이는 100 이하인 자연수입니다.
'''

def solution(mylist):
    
    answer=list(map(list,zip(*mylist)))
    return answer
  
  
'''
2차원 리스트 뒤집기 - ⭐️zip⭐️
이번 강의에서는 zip 함수를 이용해 2차원 배열을 뒤집는 방법을 알아봅시다.

다른 언어에서는..(또는 이 기능을 모르시는 분은)
보통은 다음과 같이 2중 for 문을 이용해 리스트의 row와 column을 뒤집습니다.

mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = [[], [], []]

for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        new_list[i].append(mylist[j][i])
        
python에서는
파이썬의 zip과 unpacking 을 이용하면 코드 한 줄로 리스트를 뒤집을 수 있습니다.

mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))


zip 함수에 대해
파이썬 3 한글 번역 - zip에 따르면

zip(*iterables)는 각 iterables 의 요소들을 모으는 이터레이터를 만듭니다.
튜플의 이터레이터를 돌려주는데, i 번째 튜플은 각 인자로 전달된 시퀀스나 이터러블의 i 번째 요소를 포함합니다.

영어 원문:
Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.

mylist = [1, 2, 3]
new_list = [40, 50, 60]
for i in zip(mylist, new_list):
    print (i)

(1, 40)
(2, 50)
(3, 60)


사용 예 #1 - 여러 개의 Iterable 동시에 순회할 때 사용

list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]
answer = []

for number1, number2, number3 in zip(list1, list2, list3):
   print(number1 + number2 + number3)
   
   
사용 예 #2 - Key 리스트와 Value 리스트로 딕셔너리 생성하기
파이썬의 zip 함수와 dict 생성자를 이용하면 코드 단 한 줄로, 두 리스트를 합쳐 딕셔너리로 만들 수 있습니다.

animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds)) # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
'''
