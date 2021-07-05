'''
문제 설명
base 진법으로 표기된 숫자를 10진법 숫자 출력해보세요.

입력 설명
입력으로는 공백으로 구분된 숫자가 두 개 주어집니다.
첫 번째 숫자는 num을 나타내며, 두 번째 숫자는 base를 나타냅니다.

출력 설명
base 진법으로 표기된 num을 10진법 숫자로 출력해보세요.

제한 조건
base는 10 이하인 자연수입니다.
num은 3000 이하인 자연수입니다.
예시
input	output
12 3	5
444 5	124
입출력 예 설명
입출력 예 1
3진법으로 표기된 12는 10진법으로 표현하면 5입니다. ( 1*3 + 2 )

입출력 예 2
5진법으로 표기된 444는 10진법으로 표현하면 124입니다. ( 455 + 4*5 + 4 )
'''

num, base = map(int, input().strip().split(' '))

# 내 답안 
'''
digit=len(str(num))
i=0
answer=0
while i<digit:
    answer+=(num%10)*(base**i)
    num//=10
    i+=1
print(answer)
'''

# better code
'''
answer = 0
num=str(num)
for idx, number in enumerate(num[::-1]):
    answer += int(number) * (base ** idx)
print(answer)
'''

# best code => 가장 파이썬 스러운 답안
answer=int(str(num),base)
print(answer)

