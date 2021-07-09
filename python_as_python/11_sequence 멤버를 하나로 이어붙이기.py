'''
문제 설명

문자열 리스트 mylist를 입력받아, 이 리스트의 원소를 모두 이어붙인 문자열을 리턴하는 함수, solution을 만들어주세요. 예를 들어 mylist가 ['1', '100', '33'] 인 경우, solution 함수는 '110033'을 리턴하면 됩니다.

제한 조건
mylist의 길이는 100 이하인 자연수입니다.
mylist의 원소의 길이는 100 이하인 자연수입니다.
'''

def solution(mylist):
    answer = ''.join(mylist)
    return answer
  
'''
알고리즘 문제를 풀다보면, 시퀀스의 멤버들을 하나의 string으로 이어붙여야 할 때가 있다

예시)

문자열 배열 ['1', '100', '33']을 이어 붙여 문자열 '110033' 만들기
정수형 튜플 (3, 22, 91)을 이어붙여 문자열 '32291' 만들기
다른 언어에서는..(또는 이 기능을 모르시는 분은)
보통 사람들은 for 문을 이용해 원소를 하나씩 이어 붙인다.

my_list = ['1', '100', '33']
answer = ''
for value in my_list:
    answer += value
    
    
파이썬에서는
파이썬의 str.join(iterable)을 사용하면 이 코드를 두 줄로 줄일 수 있다.

my_list = ['1', '100', '33']
answer = ''.join(my_list)
'''
