# https://www.acmicpc.net/problem/13164

# 문제요약
# N명 K그룹이 있다.
# 키차이만큼 금액이 부여됨 키 차이를 최소화 하여 그룹을 지정

# 입력
# 입력의 첫 줄에는 유치원에 있는 원생의 수를 나타내는 자연수 N(1 ≤ N ≤ 300,000)과 나누려고 하는 조의 개수를 나타내는 자연수 K(1 ≤ K ≤ N)가 공백으로 구분되어 주어진다. 다음 줄에는 원생들의 키를 나타내는 N개의 자연수가 공백으로 구분되어 줄 서 있는 순서대로 주어진다. 태양이는 원생들을 키 순서대로 줄 세웠으므로, 왼쪽에 있는 원생이 오른쪽에 있는 원생보다 크지 않다. 원생의 키는 109를 넘지 않는 자연수이다.

# 출력
# 티셔츠 만드는 비용이 최소가 되도록 K개의 조로 나누었을 때, 티셔츠 만드는 비용을 출력한다.

# 예제 입력 1 
# 5 3
# 1 3 5 6 10
# 예제 출력 1 
# 3

#문제풀이

#값을 받음.
N, K  = map(int, input().split())
H = list(map(int, input().split()))
result = [] #키차이를 저장
sum = 0

#키 차이값을 넣어줌
for i in range(1, N)  :
    result.append(H[i] - H[i-1])

#키 차이를 오름차순으로 정렬
result.sort()

#N-K만큼 은 버려짐 / 그룹으로 지정되기에 큰 차이에 따라 그룹이 나뉜다고 생각하면됨.
for i in range(N-K) :
    sum += result[i]

print(sum)


    