# T = int(input())
#
# for t in range(1,T+1):
#     k,n,m = map(int,input().split())
#     station = [0]*(n+1)
#     ch_idx = list(map(int,input().split()))
#     for i in ch_idx:
#         station[i] = k
#     fuel = k # 연료통
#     hllst = []
#     for i in range(0,len(ch_idx)-1):
#         howlong = ch_idx[i+1]-ch_idx[i]
#         hllst.append(howlong)
#     hllst.append(n-max(ch_idx))
#
#     max_l = max(hllst)
#     cnt = 0
#     for i in range(n):
#         fuel -= 1
#
#         if fuel == 0:
#             print(f'#{t} 0')
#             break
#
#         for j in hllst:
#             if fuel < j:
#                 fuel += station[i]
#                 if station[i] != 0:
#                     cnt += 1
#
#     print(f'#{t} {cnt}')

T = int(input())

for t in range(1,T+1):
    k,n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    curr , cnt = 0,0 # curr : 현재 위치 , cnt : 충전횟수
    while curr != n: # 종점에 도착할 때까지 반복
        if n <= curr + k: #curr + k : 한 번 충전으로 갈 수 있는 거리, n: 종점 까지의 거리
            curr = n #그냥 종점 도착했다 쳐도 됨. 어차피 갈 수 있으니깐
            break


        for i in range(len(arr)-1,-1,-1): #충전소 뒤에서부터 순회 why? 현재위치(curr)에서 더 적은 횟수로 가장 가까운 충저노를 먼저 찾을 수 있기 때문
            if arr[i] <= curr+k: #리스트 arr의 값이 한 번 충전으로 갈 수 있는 거리 이내에 있다면
                cnt += 1 #충전 횟수 증가
                curr = arr[i] #현재 위치를 충전소 위치로 변경
                arr = arr[i+1:] # 해당 충전소 이후의 정류장만 남기기
                break

            if i == 0: # 충전소를 찾지 못했다면
                cnt = 0
                curr = n #현재 위치를 종점으로

    print(f'#{t} {cnt}')
