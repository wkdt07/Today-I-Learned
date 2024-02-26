T = int(input())

for t in range(1,T+1):
    N,M = map(int,input().split())
    cnt = 0
    st = [0] + list(map(int,input().split())) # 인덱스 편의를 위해 맨 앞에 0을 넣어줌
    works = []
    for _ in range(M):
        work = list(map(int,input().split())) #i,j,w
        works.append(work) # 해야 되는 일 모음
    while works:
        a = works.pop(0) # 가장 먼저 들어온 일
        i,j,w = a

        if w == 1: # 1번 방법
            for k in range(i,i+j):
                if 1<=k<=N:
                    if st[k]:#검은 돌이면
                        st[k] = 0 # 흰 돌로
                    else:
                        st[k] = 1 # 흰 돌이면 검은 돌로

        if w == 2:# 2번 방법
            for k in range(i,i+j):
                if 1 <= k <= N:
                    st[k] = st[i] # j만큼 바꿔주기

        if w == 3: # 3번 방법
            for s in range(1,j+1):
                if (i-s)>=1 and (i+s)<=N:
                    if st[i-s] == st[i+s]: # 마주 보는 돌이 같은 색이면
                        if st[i-s]: # 검은 돌이면
                            st[i-s] = 0
                            st[i+s] = 0 # 둘 다 흰 돌로
                        else: # 흰 색이면
                            st[i - s] = 1
                            st[i + s] = 1 # 둘 다 검은 돌로
                    # 색이 다를 경우 그냥 넘어간다.

    st.pop(0) # 인덱스 편의를 위해 맨 앞에 넣어준 0을 제거
    print(f'#{t}',*st)

