'''
문제 설명
입력으로 0이 주어지면 영문 소문자 알파벳을, 입력으로 1이 주어지면 영문 대문자 알파벳을 사전 순으로 출력하는 코드를 짜세요.

예시 1

입력
0

출력
abcd...(중간생략)..xyz

예시 2

입력
1

출력
ABCD...(중간생략)..XYZ
'''

# 모듈 없이
'''
num = int(input().strip())
if num==0:
    for i in range(26):
        print(chr(ord('a')+i),end='')
elif num==1:
    for i in range(26):
        print(chr(ord('A')+i),end='')
'''

# 파이썬 스러운 코드 => 모듈이 존재
import string 

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789
