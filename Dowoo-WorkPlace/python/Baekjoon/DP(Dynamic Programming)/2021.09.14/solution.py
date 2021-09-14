# https://www.acmicpc.net/problem/14501

# 문제해석
# 최대값을 구하는 문제 
# 상담완료 시간과 상담수당을 줌
# 퇴사를 앞두고 있기 때문에 넘어설수는 없음

# 입력
# 첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.

# 둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며, 1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)

# 출력
# 첫째 줄에 백준이가 얻을 수 있는 최대 이익을 출력한다.

# 예제 입력 1 
# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200
# 예제 출력 1 
# 45
# 예제 입력 2 
# 10
# 1 1
# 1 2
# 1 3
# 1 4
# 1 5
# 1 6
# 1 7
# 1 8
# 1 9
# 1 10
# 예제 출력 2 
# 55
# 예제 입력 3 
# 10
# 5 10
# 5 9
# 5 8
# 5 7
# 5 6
# 5 10
# 5 9
# 5 8
# 5 7
# 5 6
# 예제 출력 3 
# 20
# 예제 입력 4 
# 10
# 5 50
# 4 40
# 3 30
# 2 20
# 1 10
# 1 10
# 2 20
# 3 30
# 4 40
# 5 50
# 예제 출력 4 
# 90

# 문제 풀이
# 뒤에서 부터 문제를 풀어나감


import sys

N = int(sys.stdin.readline())
tp=[]
dp = [0 for i in range(N+1)]

for i in range(N) :
    tp.append(list(map(int, sys.stdin.readline().split()))) 

for i in range(N-1,-1,-1): # 뒤에서 부터 시작
    if i + tp[i][0]> N : # i+소요시간이 남은날(N)보다 클경우 pass
        dp[i] = dp[i+1]
    else : # 아닐경우 현재일보상+ 현재 일이 끝난 다음날에 쌓여있는 보상 과 일을 안할경우 보상 중 최대값
        dp[i] = max(tp[i][1] + dp[i + tp[i][0]], dp[i+1])

print(dp[0])