N,T = map(int,input().split())

i_lst = list(map(int,input().split()))
i_lst.sort()
for t in range(T):
    si,ei =map(int,input().split())



def bs(i_lst,target):
    i_lst.sort()
    cnt = 0
    s = i_lst[0]
    e = i_lst[N-1]
    while s <= e:
        mid = (s + e) // 2  # 1. 중간값 찾기
        if mid > target:  # 2. mid가 target보다 크면 왼쪽 부분 탐색
            e = mid - 1

        elif A[mid] < target:  # 3. mid가 target보다 작으면 오른쪽 부분 탐색
            s = mid + 1

        elif A[mid] == target:
            cnt += 1

    return cnt