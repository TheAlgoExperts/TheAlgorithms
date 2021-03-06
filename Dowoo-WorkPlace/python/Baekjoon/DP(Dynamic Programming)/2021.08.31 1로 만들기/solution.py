# https://www.acmicpc.net/problem/1463

# 문제요약
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 최솟값

# 입력
# 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

# 출력
# 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

# 예제 입력 1 
# 2
# 예제 출력 1 
# 1
# 예제 입력 2 
# 10
# 예제 출력 2 
# 3
# 힌트
# 10의 경우에 10 -> 9 -> 3 -> 1 로 3번 만에 만들 수 있다.

# 문제풀이
# DP문제인것을 명심하자!
# 10의 경우는 10 > 5 > 4 > 2> 1 보다 10 > 9 > 3 > 1 이 최소값이다

import sys

n = int(sys.stdin.readline())
dp = [0,0,1,1] # 0~3까지는 결과를 dp list에 넣어둠

for i in range(4, n+1):

    # dp에 i번째일때 i-1 횟수에 +1한경우(즉 주어진 숫자에서 -1한경우)를 넣어줌
    dp.append(dp[i-1] +1)

    if i % 2 == 0:
        # 2로 나누어떨어질경우 위에서 저장한것과 i에 2를 나눈 나머지값의 dp에 +1한 것중 최소값을 구함
        # 4일경우 4에서 -1을하고 dp[3]을 풀은것과
        # 4/2 해서 나머지 2의 결과값에(dp[2]) +1한것중 비교해서
        # 최솟값을 구하는 것!
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        # 3도 마찬가지 방식!
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])

# 문제가 10일경우 -1을 한후 9의 결과값에 +1 해주면 최소값이 나옴
# 문제가 12일 경우 -1을 한후 11의 결과값에 +1 해주거나
# 2로 나누어 떨어지므로 -1한후 11의 결과값에 +1 것과 12/2 = 6의 결과값의 +1한 것과 비교해서 최소값을
# 3으로도 나누어 떨어지므로 2로 나누어 떨어진 최소값과 12/3 = 4의 결과값에 +1한 것과 비교해서 최소값을
# 결과값으로 보여주는것! 
