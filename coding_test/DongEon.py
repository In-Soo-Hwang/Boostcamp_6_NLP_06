# Author: DongEon, Kim.

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
# 2023-11-08
# solution 1 -> list comprehension
def solution(s):
    s = [int(x) for x in s.split()]
    return f"{min(s)} {max(s)}"

# solution 2 -> map function
def solution(s):
    s = list(map(int, s.split()))
    return f"{min(s)} {max(s)}"


# JadenCase 문자열 만들기
'''
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫번째 입출력 참고)
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

Example:
s                           return
"3people unFollowed me"     "3people Unfollowed Me"
"for the last week"         "For The Last Week"
'''
a = 'str'

# solution 1 -> use capitalize 
def solution(s):
    return ' '.join(x.capitalize().strip() for x in s.split(" "))



# 최솟값 만들기
'''
길이가 같은 배열 A, B 두개가 있습니다. 각 배열은 자연수로 이루어져 있습니다.
배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱합니다. 이러한 과정을 배열의 길이만큼 반복하며, 두 수를 곱한 값을 누적하여 더합니다. 
이때 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다. (단, 각 배열에서 k번째 숫자를 뽑았다면 다음에 k번째 숫자는 다시 뽑을 수 없습니다.)

예를 들어 A = [1, 4, 2] , B = [5, 4, 4] 라면

A에서 첫번째 숫자인 1, B에서 첫번째 숫자인 5를 뽑아 곱하여 더합니다. (누적된 값 : 0 + 5(1x5) = 5)
A에서 두번째 숫자인 4, B에서 세번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 5 + 16(4x4) = 21)
A에서 세번째 숫자인 2, B에서 두번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 21 + 8(2x4) = 29)
즉, 이 경우가 최소가 되므로 29를 return 합니다.

배열 A, B가 주어질 때 최종적으로 누적된 최솟값을 return 하는 solution 함수를 완성해 주세요.

Example:
A	        B	        answer
[1, 4, 2]	[5, 4, 4]	29
[1,2]	    [3,4]	    10
'''

# solution 2 -> list comprehension
def solution(A, B):
    answer = [x*y for x, y in zip(sorted(A), sorted(B, reverse=True))]
    return sum(answer)

 
# solution 2 -> not use list comprehension
def solution(a, b):
    a.sort(); b.sort(reverse=True)
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result


# 올바른 괄호 만들기 
'''
문제 설명
괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

제한사항
문자열 s의 길이 : 100,000 이하의 자연수
문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.


Example:
s	        answer
"()()"	    true
"(())()"	true
")()("	    false
"(()("	    false
'''

# 2023-11-09
# solution 1 -> deque 
from collections import deque 
def solution(s):
    answer = deque()
    for i in s:
        if len(answer) <= 1:
            answer.append(i)
        else:
            if i == ')' and answer[-1] == '(':
                answer.pop()
            else:        
                answer.append(i)
    if not len(answer):
        return True 
    if len(answer) == 2 and answer[0] == '(' and answer[1] == ')':
        return True 
    else:
        return False


# solution 2 -> deque / compact
from collections import deque 
def solution(s):
    answer = deque()
    for i in s:
        if not len(answer) and i == ')':
            return False
            
        if i == ')' and answer[-1] == '(':
            answer.pop()
        else:
            answer.append(i)
    if not answer :
        return True
    return False


# 이진 변환 반복하기 
'''
문제 설명
0과 1로 이루어진 어떤 문자열 x에 대한 이진 변환을 다음과 같이 정의합니다.

x의 모든 0을 제거합니다.
x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.
예를 들어, x = "0111010"이라면, x에 이진 변환을 가하면 x = "0111010" -> "1111" -> "100" 이 됩니다.

0과 1로 이루어진 문자열 s가 매개변수로 주어집니다. s가 "1"이 될 때까지 계속해서 s에 이진 변환을 가했을 때, 
이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return 하도록 solution 함수를 완성해주세요.


Example:
s	            result
"110010101001"	[3,8]
"01110"	        [3,3]
"1111111"	    [4,1]


입출력 예 #1
"110010101001"이 "1"이 될 때까지 이진 변환을 가하는 과정은 다음과 같습니다.
회차	이진 변환 이전	제거할 0의 개수	0 제거 후 길이	이진 변환 결과
1	    "110010101001"	6	            6	        "110"
2	    "110"	        1	            2	        "10"
3	    "10"	        1	            1	        "1"
3번의 이진 변환을 하는 동안 8개의 0을 제거했으므로, [3,8]을 return 해야 합니다.


입출력 예 #2
"01110"이 "1"이 될 때까지 이진 변환을 가하는 과정은 다음과 같습니다.
회차	이진 변환 이전	제거할 0의 개수	0 제거 후 길이	이진 변환 결과
1	    "01110"	        2	            3	        "11"
2	    "11"	        0	            2	        "10"
3	    "10"	        1	            1	        "1"
3번의 이진 변환을 하는 동안 3개의 0을 제거했으므로, [3,3]을 return 해야 합니다.
입출력 예 #3

"1111111"이 "1"이 될 때까지 이진 변환을 가하는 과정은 다음과 같습니다.
회차	이진 변환 이전	제거할 0의 개수	0 제거 후 길이	이진 변환 결과
1	    "1111111"	    0	            7	        "111"
2	    "111"	        0	            3	        "11"
3	    "11"	        0	            2	        "10"
4	    "10"	        1	            1	        "1"
4번의 이진 변환을 하는 동안 1개의 0을 제거했으므로, [4,1]을 return 해야 합니다.
'''

def solution(s):
    zeros, i = 0, 0
    while s != '1':
        i += 1
        zeros += s.count('0')
        s = bin(s.count('1'))[2:]
    return [i, zeros] 


# 숫자의 표현

'''
문제 설명
Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 
예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

1 + 2 + 3 + 4 + 5 = 15
4 + 5 + 6 = 15
7 + 8 = 15
15 = 15
자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

Example:
n	result
15	4
'''

# solution 1
def solution(n):
    answer = 0
    for i in range(1, n+1):
        _sum = 0
        while _sum <= n:
            _sum += i 
            i += 1
            if _sum == n:
                answer += 1
    return answer 


# 다음 큰 숫자
'''
문제 설명
자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.

Example:
n	result
78	83
15	23

입출력 예#1
문제 예시와 같습니다.
입출력 예#2
15(1111)의 다음 큰 숫자는 23(10111)입니다.
'''

# solution 1
# key point: bin()
def solution(n):
    src = bin(n)[2:].count('1')
    while True:
        n += 1
        dst = bin(n)[2:].count('1')
        if src == dst:
            return n
        
        
# 피보나치 수

'''
피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

예를들어

F(2) = F(0) + F(1) = 0 + 1 = 1
F(3) = F(1) + F(2) = 1 + 1 = 2
F(4) = F(2) + F(3) = 1 + 2 = 3
F(5) = F(3) + F(4) = 2 + 3 = 5
와 같이 이어집니다.

2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

Example:
n	return
3	2
5	5
'''

# 피보나치 수열
# solution 1
def solution(n):
    a, b = 0, 1 # starting point
    for _ in range(n):
        a, b = b, a + b # F(2), F(3) = F(0) + F(1), F(1) + F(2)
    return a % 1234567


# 짝지어 제거하기
'''
문제 설명
짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다. 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다. 
그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다. 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다. 
문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요. 성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.

예를 들어, 문자열 S = baabaa 라면

b aa baa → bb aa → aa →

의 순서로 문자열을 모두 제거할 수 있으므로 1을 반환합니다.

제한사항
문자열의 길이 : 1,000,000이하의 자연수
문자열은 모두 소문자로 이루어져 있습니다.


Example:
s	    result
baabaa	1
cdcd	0
'''

# key point: stack
# 짝지어서 ~~ -> Stack
from collections import deque 
def solution(s):
    stack = deque()
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    return int(not(stack))

def solution(s):
    stack = deque()
    for i in s:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    return int(not(stack))


# 카펫

'''
https://school.programmers.co.kr/learn/courses/30/lessons/42842

Example:
brown	yellow	return
10	    2	    [4, 3]
8	    1	    [3, 3]
24	    24	    [8, 6]
'''

# brute-force search (BFS)
def solve(n):
    answer = []
    for i in range(1, n+1):
        if not n%i:
            answer.append(i)
    return answer 

def solution(brown, yellow):
    new = solve(brown + yellow)
    for x, y in zip(new, new[::-1]):
        if (x-2) * (y-2) == yellow:
            return [y, x]
        


# 영어 끝말잇기
'''
문제 설명
1부터 n까지 번호가 붙어있는 n명의 사람이 영어 끝말잇기를 하고 있습니다. 영어 끝말잇기는 다음과 같은 규칙으로 진행됩니다.

1번부터 번호 순서대로 한 사람씩 차례대로 단어를 말합니다.
마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작합니다.
앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
이전에 등장했던 단어는 사용할 수 없습니다.
한 글자인 단어는 인정되지 않습니다.
다음은 3명이 끝말잇기를 하는 상황을 나타냅니다.

tank → kick → know → wheel → land → dream → mother → robot → tank

위 끝말잇기는 다음과 같이 진행됩니다.

1번 사람이 자신의 첫 번째 차례에 tank를 말합니다.
2번 사람이 자신의 첫 번째 차례에 kick을 말합니다.
3번 사람이 자신의 첫 번째 차례에 know를 말합니다.
1번 사람이 자신의 두 번째 차례에 wheel을 말합니다.
(계속 진행)
끝말잇기를 계속 진행해 나가다 보면, 3번 사람이 자신의 세 번째 차례에 말한 tank 라는 단어는 이전에 등장했던 단어이므로 탈락하게 됩니다.

사람의 수 n과 사람들이 순서대로 말한 단어 words 가 매개변수로 주어질 때, 
가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구해서 return 하도록 solution 함수를 완성해주세요.

Example:
n	words	                                                                                result
3	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	        [3,3]

5	["hello", "observe", "effect", "take", "either", "recognize", "encourage", 
    "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]	[0,0]
    
2	["hello", "one", "even", "never", "now", "world", "draw"]	                            [1,3]

'''

# solution 1 
def solution(n, words):
    asset = []
    for i, w in enumerate(words):
        if not asset:
            asset.append(w)
        else:
            if w in asset or asset[-1][-1] != w[0]:
                return [i%n + 1, i//n + 1]        
        asset.append(w)
    return [0, 0]
    



# 점프와 순간이동

'''
OO 연구소는 한 번에 K 칸을 앞으로 점프하거나, (현재까지 온 거리) x 2 에 해당하는 위치로 순간이동을 할 수 있는 특수한 기능을 가진 아이언 슈트를 개발하여 판매하고 있습니다. 
이 아이언 슈트는 건전지로 작동되는데, 순간이동을 하면 건전지 사용량이 줄지 않지만, 앞으로 K 칸을 점프하면 K 만큼의 건전지 사용량이 듭니다. 
그러므로 아이언 슈트를 착용하고 이동할 때는 순간 이동을 하는 것이 더 효율적입니다. 아이언 슈트 구매자는 아이언 슈트를 착용하고 거리가 N 만큼 떨어져 있는 장소로 가려고 합니다. 
단, 건전지 사용량을 줄이기 위해 점프로 이동하는 것은 최소로 하려고 합니다. 
아이언 슈트 구매자가 이동하려는 거리 N이 주어졌을 때, 사용해야 하는 건전지 사용량의 최솟값을 return하는 solution 함수를 만들어 주세요.

예를 들어 거리가 5만큼 떨어져 있는 장소로 가려고 합니다.
아이언 슈트를 입고 거리가 5만큼 떨어져 있는 장소로 갈 수 있는 경우의 수는 여러 가지입니다.

처음 위치 0 에서 5 칸을 앞으로 점프하면 바로 도착하지만, 건전지 사용량이 5 만큼 듭니다.
처음 위치 0 에서 2 칸을 앞으로 점프한 다음 순간이동 하면 (현재까지 온 거리 : 2) x 2에 해당하는 위치로 이동할 수 있으므로 위치 4로 이동합니다. 
이때 1 칸을 앞으로 점프하면 도착하므로 건전지 사용량이 3 만큼 듭니다.
처음 위치 0 에서 1 칸을 앞으로 점프한 다음 순간이동 하면 (현재까지 온 거리 : 1) x 2에 해당하는 위치로 이동할 수 있으므로 위치 2로 이동됩니다. 
이때 다시 순간이동 하면 (현재까지 온 거리 : 2) x 2 만큼 이동할 수 있으므로 위치 4로 이동합니다. 이때 1 칸을 앞으로 점프하면 도착하므로 건전지 사용량이 2 만큼 듭니다.

위의 3가지 경우 거리가 5만큼 떨어져 있는 장소로 가기 위해서 3번째 경우가 건전지 사용량이 가장 적으므로 답은 2가 됩니다.


Example:
N	    result
5	    2
6	    2
5000	5

입출력 예 #1
위의 예시와 같습니다.

입출력 예 #2
처음 위치 0 에서 1 칸을 앞으로 점프한 다음 순간이동 하면 (현재까지 온 거리 : 1) x 2에 해당하는 위치로 이동할 수 있으므로 위치 2로 이동합니다. 
이때 1 칸을 앞으로 점프하면 위치3으로 이동합니다. 이때 다시 순간이동 하면 (현재까지 온 거리 : 3) x 2 이동할 수 있으므로 위치 6에 도착합니다. 
이 경우가 건전지 사용량이 가장 적으므로 2를 반환해주면 됩니다.
'''
# solution 1
def solution(N):
    answer = 1
    while N != 1:
        if N%2:
            N -= 1
            answer += 1
        else:
            N //= 2
    return answer 


# 구명보트
'''
문제 설명
무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 
2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 
모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

제한사항
무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.

Example:
people	            limit	return
[70, 50, 80, 50]	100	    3
[70, 80, 50]	    100	    3
'''

# solution 1 -> greedy algorithm
from collections import deque 
def solution(people, limit):
    p, answer = deque(sorted(people)), 0
    while len(p) > 1:
        if p[0] + p[-1] > limit:
            p.pop()
            answer += 1
        else:
            p.pop(); p.popleft()
            answer += 1
    if p: answer += 1
    return answer 


# 예상 대진표
'''
문제 설명
△△ 게임대회가 개최되었습니다. 이 대회는 N명이 참가하고, 토너먼트 형식으로 진행됩니다.
N명의 참가자는 각각 1부터 N번을 차례대로 배정받습니다. 
그리고, 1번↔2번, 3번↔4번, ... , N-1번↔N번의 참가자끼리 게임을 진행합니다. 각 게임에서 이긴 사람은 다음 라운드에 진출할 수 있습니다. 
이때, 다음 라운드에 진출할 참가자의 번호는 다시 1번부터 N/2번을 차례대로 배정받습니다. 
만약 1번↔2번 끼리 겨루는 게임에서 2번이 승리했다면 다음 라운드에서 1번을 부여받고, 
3번↔4번에서 겨루는 게임에서 3번이 승리했다면 다음 라운드에서 2번을 부여받게 됩니다. 게임은 최종 한 명이 남을 때까지 진행됩니다.

이때, 처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지 궁금해졌습니다. 
게임 참가자 수 N, 참가자 번호 A, 경쟁자 번호 B가 함수 solution의 매개변수로 주어질 때, 
처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지 return 하는 solution 함수를 완성해 주세요. 
단, A번 참가자와 B번 참가자는 서로 붙게 되기 전까지 항상 이긴다고 가정합니다.

Example:
N	A	B	answer
8	4	7	3
'''

def solution(N, A, B):
    for i, _ in enumerate(range(N//2)):
        if abs(A-B) == 1 and (A//2) != (B//2):
            return i + 1
        A = A//2 if not A%2 else A//2 + 1
        B = B//2 if not B%2 else B//2 + 1
        
        
'''
경화는 과수원에서 귤을 수확했습니다. 경화는 수확한 귤 중 'k'개를 골라 상자 하나에 담아 판매하려고 합니다. 
그런데 수확한 귤의 크기가 일정하지 않아 보기에 좋지 않다고 생각한 경화는 귤을 크기별로 분류했을 때 서로 다른 종류의 수를 최소화하고 싶습니다.

예를 들어, 경화가 수확한 귤 8개의 크기가 [1, 3, 2, 5, 4, 5, 2, 3] 이라고 합시다. 경화가 귤 6개를 판매하고 싶다면, 
크기가 1, 4인 귤을 제외한 여섯 개의 귤을 상자에 담으면, 귤의 크기의 종류가 2, 3, 5로 총 3가지가 되며 이때가 서로 다른 종류가 최소일 때입니다.

경화가 한 상자에 담으려는 귤의 개수 k와 귤의 크기를 담은 배열 tangerine이 매개변수로 주어집니다. 
경화가 귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 return 하도록 solution 함수를 작성해주세요.
'''
        
# solution 1 -> collections.Counter
from collections import Counter
def solution(k, tangerine):
    n, answer = 0, 0
    count = Counter(tangerine)
    for v in sorted(count.values(), reverse=True):
        if n < k:
            n += v
            answer += 1
    return answer
