# 85번

#문제 
# w, h, b 가 공백을 두고 입력된다.
# 단, w, h는 모두 정수이고 1~1024 이다. b는 40이하의 4의 배수이다.

# 출력
# 필요한 저장 공간을 MB 단위로 바꾸어 출력한다.
# 단, 소수점 셋째 자리에서 반올림하여 둘째 자리까지 출력한다.

#문제풀이 : 84번 문제와 같음.


a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)

print(format('%.2f MB'%(a*b*c/8/1024/1024)))


#86번

# 입력
# 언제까지 합을 계산할 지, 정수 1개를 입력받는다.
# 단, 입력되는 자연수는 100,000,000이하이다.

# 출력
# 1, 2, 3, 4, 5 ... 순서대로 계속 더해가다가, 그 합이 입력된 정수보다 커지거나 같아지는 경우,
# 그때까지의 합을 출력한다.

#문제풀이 : 반복문사용! 

a=int(input())

n = int(0)
t = int(0)

while True : 
    t += n
    n += 1


    if t>=a :
        break

print(t)

#87번

# 입력
# 정수 1개를 입력받는다.
# (1 ~ 100)

# 출력
# 1부터 입력한 정수보다 작거나 같을 때까지 1씩 증가시켜 출력하되
# 3의 배수는 출력하지 않는다.

#문제풀이 = 반복 + if


a=int(input())

n = int(1)

while True : 
    if n % 3 !=0 :   
        print(n)
    
    n += 1

    if n>a :
        break

# 88번

# 등차수열

# 입력
# 시작 값(a), 등차의 값(d), 몇 번째 수 인지를 의미하는 정수(n)가
# 공백을 두고 입력된다.(모두 0 ~ 100)

# 출력
# n번째 수를 출력한다.

#문제풀이 : 시작값에서 계속 등차의 값을 더하고 n번째 수는 무엇인지 맞추는 문제로 for문사용

a,d,n = input().split()

a = int(a)
d = int(d)
n = int(n)

for i in range(2,n+1) : 
    a += d

print(a)

#89번 

# 등비수열

# 입력
# 시작 값(a), 등비의 값(r), 몇 번째 인지를 나타내는 정수(n)가
# 공백을 두고 입력된다.(모두 0 ~ 10)

# 출력
# n번째 수를 출력한다.

#문제풀이 : 88번과 같은데 곱하기를 할뿐 

a,d,n = input().split()

a = int(a)
d = int(d)
n = int(n)

for i in range(2,n+1) : 
    a *= d

print(a)


#90번 

# 규칙이 있는 수열

# 입력
# 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째 인지를 나타내는 정수(n)가
# 공백을 두고 입력된다.(a, m, d는 -50 ~ +50, n은 10이하의 자연수)

# 출력
# n번째 수를 출력한다.

#문제풀이 :  88.89번과 비슷한데 규칙이 더 추가됨

a,m,d,n = input().split()

a = int(a)
m = int(m)
d = int(d)
n= int(n)

for i in range(2,n+1) : 
    a *= m
    a += d 

print(a)

#91번

#최소공배수

# 입력
# 같은 날 동시에 가입한 인원 3명이 규칙적으로 방문하는,
# 방문 주기가 공백을 두고 입력된다. (단, 입력값은 100이하의 자연수이다.)

# 출력
# 3명이 다시 모두 함께 방문해 문제를 풀어보는 날(동시 가입/등업 후 며칠 후?)을 출력한다.

#문제풀이 : 최소공배수를 구하는 식 

a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)

d = int(1)

while d%a !=0 or d%b != 0 or d%c !=0 :
    d +=1

print(d)    

#92번

#갑자기 난이도가 상승했네?? 

# 출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.

# 입력
# 첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
# 두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.

# 출력
# 1번부터 번호가 불린 횟수를 순서대로 공백으로 구분하여 한 줄로 출력한다.

# 입력 예시   
# 10
# 1 3 2 2 5 6 7 4 5 9

# 출력 예시
# 1 2 1 1 2 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0


n = int(input())          #몇 개를 부를건지 값을 받음 
a = input().split()     #n개만큼 값을 받음 
arr = []                #출력할 리스트 0부터 시작하므로 0~23번까지 이므로 24개 값이 필요함

for i in range(n) :     #받은 값을 int값으로 변환 후 다시 저장해줌. a에 들어있는 것을 모두 int로 저장한다고 생각하면됨.
    a[i] = int(a[i])

for i in range(24) :    #추후에 출력위해 0으로 가득 채워줌! append(0) 사용 여기서 range 24를 적는 이유응 0부터 23까지 채우기 위해! 
    arr.append(0)

for i in range(n) :     #부른 값들을 하나씩 +1해줌 ex a[3,4,3]이라고 가정 d[3]에 +1 / d[4]에 +1 / d[3]에 +1 하라는 말
    arr[a[i]] += 1

for i in range(1, 24) : #arr[1~23]까지 출력함 arr[0]은 숫자가 0이기 때문에 제외됨. 이 부분 중요함!
    print(arr[i], end=' ')
        



























