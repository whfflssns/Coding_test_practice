### 분할 정복 알고리즘 구현(합병 정렬)
### 2개의 부분문제로 분할하고 이후에 재귀적으로 합병 정렬한 후
### 2개의 정렬된 부분을 합병하여 정렬(정복)한다.
def Merge_sort(S):
    if len(S) < 2:
        return S
    mid = int(len(S)/2)
    low_arr = Merge_sort(S[:mid])
    high_arr = Merge_sort(S[mid:])
    print(low_arr, high_arr)

    merge_arr = []
    l = r = 0
    while l < len(low_arr) and r < len(high_arr):
        if low_arr[l] < high_arr[r]:
            merge_arr.append(low_arr[l])
            l += 1
        else:
            merge_arr.append(high_arr[r])
            r += 1

    merge_arr += low_arr[l:]
    merge_arr += high_arr[r:]
    return merge_arr
    
### 이렇게 작성된 분할 정복 알고리즘(합병 정렬)도 
### 코드만 잘 작성되면 최적화를 할 수 있다.
### 병합 결과를 담은 새로운 배열을 매번 생성해서 리턴하지 않고 인덱스 접근을 이용해서 입력 배열을 계속해서 업데이트하면
### 메모리 사용량을 대폭 줄일 수 있다고 한다(코드는 인터넷에서 참고했다.)
### 또한 합병정렬의 시간복잡도는 합병의 수행시간이 합병되는 입력 크기에 비례하므로 각 층에서 수행되는 비교 횟수는 O(n)이고
### 입력 크기를 1/2로 계속해서 나누다 나눌 수 없는 1일때 분할을 중단하므로 K번 1/2번 나누면 K층이 생기고 2^K=n 이므로
### K = log2(n)임을 알 수 있다 따라서 합병 정렬 알고리즘의 시간 복잡도는 층 개수(K) * O(n) = O(nlogn)이 된다.
### 여기서 시간복잡도에서 logn은 보통 밑이 2인 것을 얘기한다.
### 밑의 코드는 최적화 하여 메모리에 문제가 발생하지 않게 하였다.

def mergeSort(list,p,q): #q= inclusive
	if p>= q: return
	mid = (p + q) // 2
	mergeSort(list, p, mid)
	mergeSort(list, mid+ 1, q)
	merge(list, p, mid + 1, q)


def merge(list, left, right, end):
	merged = []
	l, r = left, right
	while l < right and r <= end:
		if list[l] <= list[r]:
			merged.append(list[l])
			l +=1
		else:
			merged.append(list[r])
			r +=1
	while l < right:
		merged.append(list[l])
		l +=1
	while r <= end:
		merged.append(list[r])
		r+=1

	l = left
	for n in merged:
		list[l] = n	
		l +=1
