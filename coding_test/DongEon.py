# 최댓값과 최솟값 
'''
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. 
str에 나타내는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
예를 들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

Example:
s               return
"1 2 3 4"       "1 4"
"-1 -2 -3 -4"   "-4 -1"
"-1 1"          "-1 -1"
'''

# solution 1 -> list comprehension
def solution(s):
    s = [int(x) for x in s.split()]
    return f"{min(s)} {max(s)}"

# solution 2 -> map function
def solution(s):
    s = list(map(int, s.split()))
    return f"{min(s)} {max(s)}"
