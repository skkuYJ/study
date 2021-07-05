'''
문제 설명
문자열 s와 자연수 n이 입력으로 주어집니다. 문자열 s를 좌측 / 가운데 / 우측 정렬한 길이 n인 문자열을 한 줄씩 프린트해보세요.

제한조건
s의 길이는 n보다 작습니다.
(n - s의 길이)는 짝수입니다.
s는 알파벳과 숫자로만 이루어져 있으며, 공백 문자가 포함되어있지 않습니다.
입력 예
abc 7
출력 예
abc      
  abc   
    abc
'''

s, n = input().strip().split(' ')
n = int(n)

# 내 코드
'''
print(s)
print(' '*((n-len(s))//2)+s)
print((' '*(n-len(s)))+s)
'''

# 파이썬스러운 코드
s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬


# 파이썬에서는 ljust, center, rjust와 같은 string의 메소드를 사용해 코드를 획기적으로 줄일 수 있습니다.
