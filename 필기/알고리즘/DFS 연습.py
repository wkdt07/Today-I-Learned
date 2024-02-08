'''
input
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

V,E = map(int,input().split()) #V : 시작 노드 , E: 끝 노드 


'''
adjl -> 정점의 연결 여부 정리해놓은 arr(2차원) 
'''
lst = list(map(int,input().split()))
adjl = [[] for _ in range(V+1)] # adjl[i] 행에 i에 접해있는 정점 번호를 저장

# 인접 리스트
for i in range(E): 
    n1, n2 = lst[i*2],lst[i*2+1] #n1 -> 해당 노드 , n2 -> 해당 노드에 연결된 정점 (얘는 화살표가 있어서 1->2지만 화살표가 없는(방향이 없는)경우는 1->2면 2->1 동시)

    adjl[n1].append(n2)
    # adjl[n2].append(n1) 방향이 없는 경우, 1->2면 2->1 동시

    # [[],[2,3],[1,4,5],[1,7],[2,6],[2,6],[4,5,7],[6,3]]


def dfs(i,V): # 시작 i , 마지막 v
    # visited, stack 생성 및 초기화
    visited = [0]*(V+1)

    stack = []

    visited[i] = 1 # 시작점 방문, 방문하면 1
    print(i)       # 정점에 도착해서 할 일 (프린트)

    while True: # 탐색 # stack이 빌 때까지 해도 됨
        
        # 현재 방문한 정점에 인접하고, 방문 아직 안 한 정점 w가 있으면      
        for w in adjl[i]: # 인접 정점들
            if visited[w] == 0: # 방문한 적 없으면, 방문하면 1이었음
                stack.append(i) #이전 노드 i를 스택에 추가
                i = w # w를 시작점으로. w에 방문
                visited[i] = 1 # 방문 기록 (w로 갱신된 i)
                print(i) # 방문했으니깐 프린트
                break # for w에 대한 break
            
        else: # 더 이상 갈 길이 없으면
                 #스택이 비어 있지 않으면(지나온 정점이 남아 있으면) -> 거기서부터 다시 시작하면 됨
            if stack: # 비어있으면 False, 아니면 True
                i = stack.pop() # 이전으로 돌아가기
                
            else: # 스택이 비어있으면(출발점에서 남은 정점이 없으면) -> 거슬러 올라간거임
                break # while에 대한 break



dfs(1,8) # 1번부터 돌아봐라