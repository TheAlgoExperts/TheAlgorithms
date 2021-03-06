# https://www.acmicpc.net/problem/1149

# 문제요약
# RGB로 색을 칠함
# 앞뒤로 다른 색이어야함
# 가격이 주어지는데 최솟값을 구하라

# 입력
# 첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

# 예제 입력 1 
# 3
# 26 40 83
# 49 60 57
# 13 89 99
# 예제 출력 1 
# 96

#문제풀이

import sys

N = int(sys.stdin.readline())
C = [] # 색의 값을 담음

for i in range(N) : # 기본 값을 담음
    C.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N) : # 두번째 색부터 앞에 껄 더해주는 작업!
    C[i][0] = min(C[i-1][1], C[i-1][2]) + C[i][0] # 두번째의 첫번째 색을 골랏을때 2,3중 최소값
    C[i][1] = min(C[i-1][0], C[i-1][2]) + C[i][1] # 두번째의 두번째 색을 골랏을때 1,3중 최소값
    C[i][2] = min(C[i-1][0], C[i-1][1]) + C[i][2] # 두번째의 세번째 색을 골랏을때 1,2중 최소값

#그중의 최소값을 출력!
print(min(C[N-1]))
