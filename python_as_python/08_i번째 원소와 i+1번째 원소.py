'''
문제 설명

숫자를 담은 리스트 mylist가 solution 함수의 파라미터로 주어집니다. solution 함수가 mylist의 i번째 원소와 i+1번째 원소의 차를 담은 일차원 리스트에 차례로 담아 리턴하도록 코드를 작성해주세요.

단, 마지막에 있는 원소는 (마지막+1)번째의 원소와의 차를 구할 수 없으니, 이 값은 구하지 않습니다.

제한 조건
mylist의 길이는 1 이상 100 이하인 자연수입니다.
mylist의 원소는 1 이상 100 이하인 자연수입니다.

예시
mylist	output
[83, 48, 13, 4, 71, 11]	[35, 35, 9, 67, 60]

설명:
83과 48의 차는 35입니다.
48과 13의 차는 35입니다.
13과 4의 차는 9입니다.
4와 71의 차는 67입니다.
71과 11의 차는 60입니다.
따라서 [35, 35, 9, 67, 60]를 리턴합니다.
'''

def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer


'''
다른 언어에서는..(또는 이 기능을 모르시는 분은)
보통은 다음과 같이 len과 index를 이용하여 각 원소에 접근한다.

def solution(mylist):
    answer = []
    for i in range(len(mylist)-1):
        answer.append(abs(mylist[i] - mylist[i+1]))
    return answer

if __name__ == '__main__':
    mylist = [83, 48, 13, 4, 71, 11]    
    print(solution(mylist))
    
    
하지만 python에서는,
파이썬의 zip을 이용하면 index를 사용하지 않고 각 원소에 접근할 수 있다.



if __name__ == '__main__':
    mylist = [83, 48, 13, 4, 71, 11]    
    print(solution(mylist))
    
※ 주의

zip 함수에 서로 길이가 다른 리스트가 인자로 들어오는 경우에는 길이가 짧은 쪽 까지만 이터레이션이 이루어진다.
'''
