'''
문제 설명

숫자를 담은 일차원 리스트, mylist에 대해 mylist의 원소로 이루어진 모든 순열을 사전순으로 리턴하는 함수 solution을 완성해주세요.

제한 조건
mylist 의 길이는 1 이상 100 이하인 자연수입니다.

예시
mylist	output
[2, 1]	[[1, 2], [2, 1]]
[1, 2, 3]	[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
'''

def solution(mylist):
    import itertools
    answer = list(itertools.permutations(mylist))
    answer.sort()
    return answer
  
'''
순열과 조합 - combinations, permutations
이번 강의에서는 iterable의 원소로 순열과 조합을 구하는 방법을 배워보자.

예시)
1,2,3의 숫자가 적힌 카드가 있을 때, 이 중 두 장을 꺼내는 경우의 수 -> 12, 13, 21, 23, 31, 32
'A', 'B', 'C'로 만들 수 있는 경우의 수 -> 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'

다른 언어에서는..(또는 이 기능을 모르시는 분은)
보통 사람들은 for 문을 이용해 permutation 함수를 구현한다.

def permute(arr): # [3, 1, 2]
    result = [arr[:]]  # [[1, 3, 2], [3, 1, 2], [2, 1, 3], [3, 1, 2]]
    c = [0] * len(arr) # [0, 0, 0]
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result


하지만 파이썬에서는
itertools.permutation를 이용하면, for문을 사용하지 않고도 순열을 구할 수 있다.

import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기

※ 조합은 itertools.combinations를 사용해서 구할 수 있습니다. 사용법은 permutations와 비슷해요!
'''
