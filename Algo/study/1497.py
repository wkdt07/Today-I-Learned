import sys
input = sys.stdin.readline

N,M = map(int,input().split()) # N:기타갯수 M: 곡 갯수

song= []
for _ in range(N):
    a,b = input().split()
    song.append(b)

vst_guitar = [0]*N
vst_song = [0]*M
# 그냥 백트래킹으로 완전탐색 해도 상관 없을거 같다.

# vst_g = [] # 곡 사용한거 있는지 여부
max_v = -1 # 최대 곡수
cnt = 0 # 사용된 기타 갯수
g_min = float('inf')
def bt(cnt = 0,song_cnt = 0):
    global max_v
    global g_min
    global vst_song

    if song_cnt == max_v: # 값이 같다면
        g_min = min(g_min,cnt)

    if song_cnt > max_v: # 칠 수 있는 곡이 더 많아지면
        max_v = song_cnt
        g_min = cnt


    if cnt == N:
        if max_v == 0:
            g_min = -1
            return

    # if max_v == M:
    #     return

    for i in range(N):
        if not vst_guitar[i]:
            vst_guitar[i] = 1

            vst_song_prev = vst_song[:]
            temp = 0
            for j in range(M):
                if song[i][j] == 'Y' and not vst_song[j]:
                    vst_song[j] = 1
                    temp += 1
            bt(cnt+1,song_cnt + temp)
            vst_song = vst_song_prev
            vst_guitar[i] -= 1

bt()
print(g_min)





