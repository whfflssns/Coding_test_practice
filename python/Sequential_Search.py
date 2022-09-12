### 순차 탐색 알고리즘 작성하기(최대 숫자 찾기)
a = list(map(int, input().split()))
x = a[0]
for i in range(1, len(a)):
    if a[i] > x:
        x = a[i]
print(x)
