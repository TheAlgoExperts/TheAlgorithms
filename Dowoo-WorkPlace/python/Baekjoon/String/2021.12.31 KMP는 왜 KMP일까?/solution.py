# https://www.acmicpc.net/problem/2902

# 문제풀이
# 앞에 대문자를 대표문자로 생각하여 축약해서 출력

# 입력
# 입력은 한 줄로 이루어져 있고, 최대 100글자의 영어 알파벳 대문자, 소문자, 그리고 하이픈 ('-', 아스키코드 45)로만 이루어져 있다. 첫 번째 글자는 항상 대문자이다. 그리고, 하이픈 뒤에는 반드시 대문자이다. 그 외의 모든 문자는 모두 소문자이다.

# 출력
# 첫 줄에 짧은 형태 이름을 출력한다.

# 예제 입력 1 
# Knuth-Morris-Pratt
# 예제 출력 1 
# KMP
# 예제 입력 2 
# Mirko-Slavko
# 예제 출력 2 
# MS
# 예제 입력 3 
# Pasko-Patak
# 예제 출력 3 
# PP

# 문제풀이
# 2021년 마지막 문제풀이! 쉬운문제차례

a = list(input().split('-'))
for i in a :
    print(i[0], end = '')


# 한줄코딩 
# 필터를 사용해서 대문자인것만 골라서 출력
# *는 []벗겨냄

print(*filter(str.isupper,input()),sep='')