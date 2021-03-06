# https://www.acmicpc.net/problem/11057

# 문제요약
# 오르차순으로 수를 이룬다
# 갯수를 구하라

# 입력
# 첫째 줄에 N (1 ≤ N ≤ 1,000)이 주어진다.

# 출력
# 첫째 줄에 길이가 N인 오르막 수의 개수를 10,007로 나눈 나머지를 출력한다.

# 예제 입력 1 
# 1
# 예제 출력 1 
# 10
# 예제 입력 2 
# 2
# 예제 출력 2 
# 55
# 예제 입력 3 
# 3
# 예제 출력 3 
# 220

# 문제풀이
# 숫자 0부터 넣을때 
# N = 1는 1,1,1,1,1~ 이렇게 진행(0,1,2,3,4,~)
# N = 2는 1,2,3,4,5~ 이렇게 진행(0,01/11, 02/12/22~)
# N = 3는 1,3,5,8,14~ 이렇게 진행(0,001/011/111 ~)
# 계산식이 dp[i][j] = dp[i-1][j]+dp[i][j-1]로 확인


import sys

N = int(sys.stdin.readline())
dp = [[1 for _ in range(10)] for _ in range(N+1)] # 전체 1로 넣어줌

for i in range(2, N+1) : # N =2부터
    for j in range(1,10) :  # 0은 무조건 1개 이므로 1부터 진행
        dp[i][j] = dp[i-1][j]+dp[i][j-1]

print(sum(dp[N])%10007)

