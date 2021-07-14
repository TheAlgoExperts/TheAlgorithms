#https://www.acmicpc.net/problem/1931

#이 문제는 내가 알고 있는 것에서 벗어남 느낌.. 너무 어려움. 찾아보고 해결! lambda로 이중 정렬을 해야함! 

# 문제요약
# 1개의 회의실 존재함 
# N개의 회의에 대해서 회의실 사용표를 만들고자함.
# 각회의 I에 대해 시작과 끝시간이 주어짐.
# 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 갯수를 구하는 것.
#단 회의의 시작과 끝나는 시간이 같을 수 있음.

# 입력
# 첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 시작 시간과 끝나는 시간은 231-1보다 작거나 같은 자연수 또는 0이다.

# 출력
# 첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.

# 예제 입력 1 
# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14

# 예제 출력 1 
# 4

#문제풀이
#1.n = 회의 수 / arr = 각 회의별 시간 담을 list / count = 회의수 / last = 마지막 시간
n = int(input())
arr = []
count = 0
last = 0 

#2. 값을 받아서 리스트에 넣어줌
for i in range(n) : 
    arr.append(list(map(int,input().split())))

#3. <포인트> laambda를 활용해서 끝나는 순 / 시작순으로 정렬  : 끝나는 순으로 정리하는 이유는 최대회의 수 이기 떄문에 빨리 끝나야함
arr.sort(key=lambda x:(x[1], x[0]))

#4. arr 기준으로 시작시간이 끝나는 시간과 같거나 클경우 회의 수 추가하고 그에 해당하는 끝나는 시간을 last에 넣어줌
for i in arr:
    if i[0] >= last : 
        count += 1
        last = i[1]

#5. 출력 
print(count)

