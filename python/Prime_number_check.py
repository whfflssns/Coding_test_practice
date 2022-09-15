### 에라토스테네스의 체(소수 판별하기)
### 처음에 원하는 크기만큼의 배열을 선언하여 각 값을 넣어 초기화한다.
### 2부터 시작하여 특정 수의 배수에 해당하는 수를 모두 지운다.(자기자신을 제외하고, 이미 지워진 수는 건너뛴다)
### 2부터 시작하여 남아있는 수를 모두 출력한다.
a = [i for i in range(10000)]
for i in range(2, 10000):
    if a[i] == 0:
        continue
    for j in range(i*2, 10000, i):
        a[j] = 0

for i in range(2, 10000):
    if a[i] != 0:
        print(a[i])

### 위의 값들은 내가 직접 작성한 것이고 밑에 있는 코드는 위키에 있는 코드를 가지고 왔다.
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]
