# https://www.acmicpc.net/problem/16953

# 문제요약
# a>b로 가야함 
# x2를 하거나 뒤에 1을 추가한다

# 입력
# 첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.

# 출력
# A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.

# 예제 입력 1 
# 2 162
# 예제 출력 1 
# 5
# 2 → 4 → 8 → 81 → 162

# 예제 입력 2 
# 4 42
# 예제 출력 2 
# -1
# 예제 입력 3 
# 100 40021
# 예제 출력 3 
# 5

# 문제풀이

# 이 문제는 거꾸로 풀어야한다. 

# 숫자를 받는다
a, b = map(int, input().split())
result = 1 # 처음에 결과값에 1을 더한다고 했으니 1

while True : 
    if a == b : #같으면 스탑!
        break
     # 여기서 부터 중요함! 2로 나눠서 0이 아닐경우 2배수가 아님 / 10으로 나눠서 나머지가 1이 아닐경우 뒤에+1조건 불가능 / 처음 크기가 큰경우 불가능
    elif (b%2 != 0 and b%10 != 1) or (b<a) :
        result = -1
        break
    else :
        if b % 10 == 1 : # 10으로 나눠서 나머지가 1이 1인경우 즉 뒤에 1을 붙여주는 경우임
            b = b//10
            result += 1
        else :
            b = b // 2 # 2를 나눠서 0인 경우는 2배를 한거임
            result +=1

print(result)