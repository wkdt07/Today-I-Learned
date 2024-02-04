arr = [7,2,5,3,1,4]
def asc(arr, n): #오름차순
    # for i : n-1 -> 1 (구간의 끝, 마지막 인덱스, 원소가 정렬될 위치)
    # for i in range(n-1, 0, -1): #(끝이 1이라, 쓰는건 0)
    # # for j : 0 -> i-1 , j는 비교할 두 원소 주 왼쪽 원소의 인덱스
    for j in range(0,n):
        if arr[j] > arr[j+1]: #오름차순은 큰 수를 오른쪽으로
            arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


print(asc(arr,1))