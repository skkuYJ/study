'''
문제 설명

이 문제에는 표준 입력으로 문자열, mystr이 주어집니다. mystr에서 가장 많이 등장하는 알파벳만을 사전 순으로 출력하는 코드를 작성해주세요.

제한 조건
mystr의 원소는 알파벳 소문자로만 주어집니다.
mystr의 길이는 1 이상 100 이하입니다.

예시
input	output
'aab'	'a'
'dfdefdgf'	'df'
'bbaa'	'ab'
'''

my_str = input().strip()
freq={}
for alp in my_str:
    if alp in freq:
        freq[alp]+=1
    else:
        freq[alp]=1
Max=0
answer=[]
for alp in freq:
    if freq[alp]>Max:
        Max=freq[alp]
        answer=[alp]
    elif freq[alp]==Max:
        answer.append(alp)
answer.sort()
print(''.join(answer))

'''
가장 많이 등장하는 알파벳 찾기 - Counter
알고리즘 문제를 풀다 보면 어떤 원소 x가 주어진 시퀀스타입에 몇 번이나 등장하는지 세야 할 때가 있습니다.
이런 경우는 보통 어떻게 하시나요?

다른 언어에서는..(또는 이 기능을 모르시는 분은)
보통 사람들은 반복문을 이용해 수를 셉니다.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = {}
for number in my_list:
    try:
        answer[number] += 1
    except KeyError:
        answer[number] = 1

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100])  # =  raise KeyError
파이썬에서는
파이썬의 collections.Counter 클래스를 사용하면 이 코드를 간략하게 만들 수 있습니다.

import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100]) # = 0
'''
