# https://www.acmicpc.net/problem/2178

# NxM 배열로 표현되는 미로가 있다.
# 1은 이동가능 0은 이동 불가능
# N,M으로 이동할떄 지나야 하는 최소의 칸수를 구하라 인접한 칸만 이동가능

# 입력
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

# 출력
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

# 예제 입력 1 
# 4 6
# 101111
# 101010
# 101011
# 111011
# 예제 출력 1 
# 15
# 예제 입력 2 
# 4 6
# 110110
# 110110
# 111111
# 111101
# 예제 출력 2 
# 9
# 예제 입력 3 
# 2 25
# 1011101110111011101110111
# 1110111011101110111011101
# 예제 출력 3 
# 38
# 예제 입력 4 
# 7 7
# 1011111
# 1110001
# 1000001
# 1000001
# 1000001
# 1000001
# 1111111
# 예제 출력 4 
# 13

# 문제풀이
# 이런문제는 dp로도 많이 해봤지만 상하좌우 움직임, 중복해서 더할 필요도 없음 그래서 dp사용 안함.
# 최단경로찾기 이므로 넓이우선탐색인 BFS로 찾는다.


N, M = map(int, input().split()) 
miro = [list(input()) for _ in range(N)] #여기서 문자 그대로 받음 str임

# 상하좌우
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

miro[0][0] = 1 # 0,0을 숫자로 변환시켜줌 추후에 더할 수 있게끔 / 만약 숫자로 변환된거는 방문한 것이기 때문에 다시 안감.
q = [(0,0)] #시작할 좌표

while q :
    print(q)
    a,b = q.pop(0) # a=0,  b=0 이되어버림

    for i in range(4): # 상하좌우로 이동
        x = a + dx[i]
        y = b + dy[i]
        
        if 0 <= x < N and 0 <= y < M and miro[x][y] == "1": # 문자 1일경우 방문 안한것!
            q.append((x,y)) #해당 좌표를 추가시킴
            miro[x][y] = miro[a][b]+1

print(miro[-1][-1])

