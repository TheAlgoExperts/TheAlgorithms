## Python Useful Method

### πββοΈ μ€μ μκ³ λ¦¬μ¦ μ ν μ λ¦¬

1. [Greedy](https://github.com/jasper-oh/coding-test-algorithm)
2. [DFS/BDS](https://github.com/jasper-oh/coding-test-algorithm)
3. [Sort](https://github.com/jasper-oh/coding-test-algorithm)
4. [Binary Searching](https://github.com/jasper-oh/coding-test-algorithm)
5. [Dynamic Programming](https://github.com/jasper-oh/coding-test-algorithm)
6. [Short Path](https://github.com/jasper-oh/coding-test-algorithm)
7. [Graph](https://github.com/jasper-oh/coding-test-algorithm)

### πββοΈ Context

1. μ€μλ©μλ μ λ¦¬
2. λλ€ννμ
3. ...

### πββοΈ μ€μ λ©μλ μ λ¦¬ ( μΆν λμ΄λλ©΄ PDF μ λ¦¬ μμ  )

#### 2021-07-01

count(n) -> ν΄λΉ λ°°μ΄ μμ n μ΄ λͺκ° λ€μ΄μλμ§ νμΈν΄ μ£Όλ λ©μλ
[νμΈ](https://www.geeksforgeeks.org/python-list-function-count/)

#### 2021-07-02

λ°°μ΄μ μ€λ³΅μ μ κ±° ν λλ list(set(array)) λ‘ μ§ν© ννλ‘ λ³ν ν νμ λ€λ₯Έ λ°°μ΄λ‘ λ§λ€μ΄ λ²λ¦¬λ©΄ κ°λ¨νλ€.

#### 2021-07-05

a = bin(arr1[i] | arr2[i])[2:]

10 μ§μλ₯Ό 2μ§μλ‘ λ°κΎΌ λ€μ, or μ°μ°μ μ²λ¦¬ν΄μ€λ€.

π¬ and operator => x & y
π¬ not operator => ~ x
π¬ XOR operator => x ^ y

#### 2021-07-09

```python

#  μ¬λ―Έ μΌμ λ§λ€μ΄ λ³Έ ν΄λΉ list μμ μλ μμκ° list μΈμ§ μλμ§ νλ¨νλ€μ
#  list λΌλ©΄, λ΄λΆλ‘ μ§μνλ©°, λ§μ½ list νμ΄ μλλΌλ©΄,
#  μΆλ ₯ νλ ννμ λ§€μλ
var = [1, 2, ['a', 'b', ['Dream', "TRUE"]]]


def getArrayElement(var):
    for i in range(len(var)):
        if type(var[i]) != list:
            print(var[i])
        else:
            for j in range(len(var[i])):
                if type(var[i][j]) != list:
                    print(var[i][j])
                else:
                    for k in range(len(var[i][j])):
                        print(var[i][j][k])
```

#### 2021-08-31

JOIN ν¨μ μ λ¦¬
λ¬Έμμ΄μ λ€λ£°λ μ μ©νκ² μ¬μ©λλ ν¨μ.

```python

'κ΅¬λΆμ'.join(list)

'_'.join(["something" , "hello"])

# something_hello

```

#### 2021-09-01

Numpy μ λ¦¬

```python

import numpy as np

# numpy κΈ°λ³Έ μ¬μ©λ²
array = np.array([1,2,3])

print(array.size)
print(array.dtype)
print(array[2])

# numpyλ‘ λ°°μ΄ λ§λ€κΈ°

array1 = np.arange(4)

# Numpy λ‘ λ°°μ΄ ν©μΉκΈ°
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.concatenate([arr1 , arr2])

# λ°°μ΄μ νν λ°κΎΈκΈ°

arr1 = np.array([1,2,3,4])
arr2 = arr1.reshape((2,2))

print(arr2.shape)

# numpy λ°°μ΄μ μΈλ‘ μΆμΌλ‘ ν©μΉκΈ°

arr1 = np.arange(4).reshape(1,4)
arr2 = np.arange(8).reshape(2,4)

arr3 = np.concatenate([arr1 , arr2], axis = 0)
print(arr3.shape)

# numpy λ°°μ΄μ λλκΈ°

numpy λ°°μ΄μ λλλμλ split() ν¨μλ₯Ό μ¬μ©νλ©° μ΄λ concatenate() ν¨μμ ν‘μ¬νκ² λμνλ€.
2 x 4 λ°°μ΄μ μΌμͺ½κ³Ό μ€λ₯Έμͺ½μΌλ‘ μ΄λ±λΆνλ μ½λ
```

```python

array = np.arange(8).reshape(2,4)
left ,right = np.split(array , [2] , axis = 1)
print(left.shape)
print(right.shape)
print(right[1][1])

```

```python

# numpy νλ ¬μ κ³±

answer = (np.matrix(arr1) * np.matrix(arr2)).tolist()

```

mapμΌλ‘ ν λ³νκΉμ§ νλ©° list λ‘ λ³ν

```python

s = "1 2 3 4"

arr_s = list(map(int, s.split()))

# arr_s = [1,2,3,4]

```

μ§λ² λ¬Έμ κ° λμ¬κ²½μ° μ΄κ±Έ μκ°νλ€.

```python

def get_digits(λ°κΎΈκ³  μΆμ 10μ§λ²μ μ«μ = n , λͺμ§λ² = k):
    temp = "0123456789ABCDEF"

    i , j = divmod(n , k)

    if i == 0:
        return temp[j]
    else:
        return get_digits(i , k) + temp[j]

```

### λλ€ ννμ

> λλ€ ννμ μ΄λ?

μΈκ³΅μ§λ₯ λΆμΌλ Auto CAD λΌλ μ€κ³ νλ‘κ·Έλ¨μμ μ°μ΄λ Lisp λΌλ μΈμ΄μμ λ¬Όλ € λ°μλ€κ³  νλ€.

ν¨μλ₯Ό λ± ν μ€ λ§μΌλ‘ λ§λ€κ² ν΄μ€λ€.

> νμμ ?

lamda μΈμ : ννμ

> > λμλ₯Ό λν ν¨μλ‘ μμ

> > > μΌλ° ν¨μ

```python

def hap( x , y ){
    return x + y
}

hap(10, 20)

# 30

```

> > > λλ€ νμ

```python

(lambda x, y: x + y)(10, 20)

# 30

# ν¨μ μ΄λ¦μ΄ μλΉ ..?

```

> > Map() ν¨μ

map(ν¨μ , λ¦¬μ€νΈ)

μ΄ ν¨μλ ν¨μμ λ¦¬μ€νΈλ₯Ό μΈμλ‘ λ°λλ€.

```python

# python 2
map(lambda x: x ** 2 , range(5))

# python 3

list(map(lambda x: x ** 2 , range(5)))

# 2 μ 3 λͺ¨λ [0,1,4,9,16]

```

> > reduce() ν¨μ

reduce(ν¨μ, μνΈμ€)

μνΈμ€(λ¬Έμμ΄, λ¦¬μ€νΈ, νν)μ μμλ€μ λμ μ μΌλ‘ ν¨μλ₯Ό μ μ©μν¨λ€κ³  νλ€.

```python
# python 3 μμλ μ¨μΌ νλ€.
from functools import reduce
reduce(lambda x, y : x + y , [0,1,2,3,4])

# 10

# μμ μμ λ λ¨Όμ  0κ³Ό 1μ λνκ³ , κ·Έ κ²°κ³Όμ sequence μ μλ κ°μ μ°¨λ‘λ‘ λν΄μ£Όλ κ°μ μ΄μΌκΈ°νλ€.

reduce(lambda x, y : y + x , 'abcde')

# 'edcba'

```

> > filter()

filter(ν¨μ , λ¦¬μ€νΈ)

λ¦¬μ€νΈμ λ€μ΄μλ μμλ€μ ν¨μμ μ μ©μμΌμ κ²°κ³Όκ° μ°ΈμΈ κ°λ€λ‘ μλ‘μ΄ λ¦¬μ€νΈλ₯Ό λ§λ€μ΄ μ€λ€. 0 λΆν° 9 κΉμ§μ λ¦¬μ€νΈ μ€μμ 5λ³΄λ€ μμ κ²λ§ λλ € μ£Όλ μμ 

```python
# python 2
filter(lambda x : x < 5 ,range(10))

# python 3
list(filter(lambda x : x < 5 ,range(10)))

#  [0,1,2,3,4]


```

```

```
