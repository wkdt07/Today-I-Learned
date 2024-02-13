T = int(input())

def bt(s,e):
    global S
    stack = []
    stack.append(s) # 시작 지역 저장
    while True:
        if arr[s] == [] or visited[s] ==1:
            s = stack.pop()
            if stack == []: # 더이상 돌아갈 곳이 없으면. 어차피 시작할 때 시작 지역이 stack에 연속으로 있어도 visited가 1이라 다 빠짐
                break
        else:
            visited[s] = 1 # 출근 도장
            for k in arr[s]:
                stack.append(s) # 이전 지역을 저장
                s = k
                if s == e: # 목적지에 도착하면
                    return 1

                if s == S: # 무한 루프 빠지면 ex) 1->5->7->3->1
                    break
                continue

    return 0


for t in range(1,T+1):
    V,E = map(int,input().split())

    arr = [[] for v in range(V+1)]

    for e in range(E): # arr에 노드와 경로 저장
        a,b = map(int,input().split())
        arr[a].append(b)

    S,G = map(int,input().split()) # 시작과 끝

    visited = [0] * (V + 1) # 출근도장 제작

    result = bt(S,G)

    print(f'#{t} {result}')


