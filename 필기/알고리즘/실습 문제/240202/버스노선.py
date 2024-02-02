# T = int(input())
#
# for t in range(1,T+1):
#     N= int(input())
#     cnt = [0]*5001 # 5000번 정류장까지
#
#     #N개의 노선을 정류장에 표시
#     for i in range(N):
#         A , B = map(int,input().split())
#         for j in range(A,B+1): # 이 문제에선 아니지만, 가끔 A와 B의 크기가 반대일 수 있다. 그러니깐
#             # 둘 크기를 비교하고 넣어야 하는 경우도 존재. 주의
#             cnt[j] += 1
#
#         P = int(input())
#         busstop = [int(input()) for _ in range(P)]
#         print(f'#{t}', end = ' ')
#         for i in busstop: # 출력할 정류장 번호
#             print(cnt[i], end = ' ')
# # 주의! 이러면 다음 테스트케이스도 일렬로 나옴. 그러니깐 테스트 케이스 하나인 문제는 복붙해서 하나 더 만들어라
#         print()
#
# # 리스트 하나하나 돌면서 cnt+=1 하면 수가 많아지면 시간 오류 날 수 있다
T = int(input())

for t in range(1,T+1):
    N = int(input())
    bus = [0]*(5001)
    for n in range(N):
        A,B = map(int,input().split())
        for i in range(A,B+1):
            bus[i] += 1
    P = int(input())

    station = []
    for p in range(P):
        station.append(int(input()))

    result = []
    for s in station:
        result.append(bus[s])


    print(f'#{t}',*result)
