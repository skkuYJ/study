'''
문제 설명

문자열을 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. solution 함수가 mylist를 일차원 리스트로 만들어 리턴하도록 코드를 작성해주세요.

제한 조건
arr의 길이는 1 이상 100 이하인 자연수입니다.
arr 원소의 길이는 5를 넘지 않습니다.

예시
input	output
[[1], [2]]	[1, 2]
[['A', 'B'], ['X', 'Y'], ['1']]	['A', 'B', 'X' ,'Y', '1']
'''

def solution(mylist):
    answer = sum(mylist,[])
    #answer=[element for array in mylist for element in array]
    return answer
  
'''

2차원 리스트를 1차원 리스트로 만들기 - from_iterable
코딩을 하다 보면, 이차원 리스트를 일차원 리스트로 만들어야 할 때가 있다. 이럴 땐 어떻게 하시나요?

다른 언어에서는..(또는 이 기능을 모르시는 분은)
보통 사람들은 반복문을 이용해 리스트를 더해간다.

my_list = [[1, 2], [3, 4], [5, 6]]
answer = []
for element in my_list:
    answer += element
    
하지만 파이썬에서는
파이썬의 다양한 기능을 사용하면, for 문을 사용하지 않고도 리스트를 이어 붙일 수 있다.

my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법 2 - itertools.chain
import itertools
list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools와 unpacking
import itertools
list(itertools.chain(*my_list))

# 방법 4 - list comprehension 이용
[element for array in my_list for element in array]

# 방법 5 - reduce 함수 이용 1
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))

# 방법 6 - reduce 함수 이용 2
from functools import reduce
import operator
list(reduce(operator.add, my_list))


제한적으로 사용 가능한 방법
아래의 방법은 각 원소의 길이가 동일한 경우에만 사용 가능하다.

# 방법 7 - numpy 라이브러리의 flatten 이용
import numpy as np
np.array(my_list).flatten().tolist()
예를 들어 다음과 같은 리스트는 편평하게 만들 수 있고

[[1], [2]]
[[1, 2], [2, 3], [4, 5]]

다음과 같이 같이 각 원소의 길이가 다른 리스트는 편평하게 만들 수 없다.

[['A', 'B'], ['X', 'Y'], ['1']]
'''
