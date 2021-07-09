'''
문제 설명

정수를 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. solution 함수가 mylist 각 원소의 길이를 담은 리스트를 리턴하도록 빈칸을 완성해보세요.

hint) 이전 강의에서 배운 map 함수를 활용해보세요

제한 조건
mylist의 길이는 100 이하인 자연수입니다.
mylist 각 원소의 길이는 100 이하인 자연수입니다.

예시
input	output
[[1], [2]]	[1, 1]
[[1, 2], [3, 4], [5]]	[2, 2, 1]
'''

def solution(mylist):
    answer = list(map(len, mylist))
    return answer
