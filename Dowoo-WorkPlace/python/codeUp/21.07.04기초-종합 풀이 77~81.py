#77번 
#정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

n = int(input())
s = 0
for i in range(1, n+1) :
  if i%2==0 :
    s += i

print(s)


# 78번 
# 영문 소문자 'q'가 입력될 때까지
# 입력한 문자를 계속 출력하는 프로그램을 작성해보자.

a = 'a'
while a!='q' : 
    a = input()
    print(a)


#79번

# 1, 2, 3 ... 을 계속 더해 나갈 때,
# 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
# 계속 더하는 프로그램을 작성해보자.


a = int(input())
i = 0
t = 0 

while t<a :
    i +=1
    t= t+i

print(i)  


#80번

# 1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때,
# 나올 수 있는 모든 경우를 출력해보자.

n = int(input())
m = int(input())

for i in range(1,n+1):
    for j in range(1,m+1) :
        print(i,j)



#81번

# 16진수(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)를 배운
# 영일이는 16진수끼리 곱하는 16진수 구구단?에 대해서 궁금해졌다.

# A, B, C, D, E, F 중 하나가 입력될 때,
# 1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
# (단, A ~ F 까지만 입력된다.)


a = int(input(),16) 

for i in range(1, 16): 
    print('%X*%X=%X'%(a,i,a*i))



    

