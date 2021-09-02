# https://www.acmicpc.net/problem/11726

# 문제요약
# 2xn 크기의 직사각형을 1x2, 2x1타일로 채우는 방법의 수를 구하라
# 출력할때 10,007을 나눈 나머지!

# 입력
# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

# 출력
# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

# 예제 입력 1 
# 2
# 예제 출력 1 
# 2
# 예제 입력 2 
# 9
# 예제 출력 2 
# 55

#문제풀이 하나씩 풀어나가니 결국 피보나치수열

import sys

N = int(sys.stdin.readline())
dp = [0,1,2,3,5] # dp에 담아두기

for i in range(5,N+1) :
    dp.append(dp[i-1]+dp[i-2]) # 점화식 넣기

print(dp[N]%10007) # 나머지 출력!