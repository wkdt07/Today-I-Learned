'''
2친구이기 위한 조건
1. 본인의 친구거나
2. 친구의 친구거나

주의:
1. 1친구와 2친구가 겹칠 수 있음 -> set()으로
2. 본인은 친구로 세면 안됨 -> 마지막 크기에서 1을 빼던가(어차피 무조건 한 번 센다),
'''


N = int(input())

arr = [input().strip() for _ in range(N)]
ans = 0
for i in range(N): # 본인
    cnt_2 = set()
    for j in range(N):
        if arr[i][j] == 'Y':

            cnt_2.add(j)

            for k in range(N):
                if arr[j][k] == 'Y':
                    if i == k: # 본인 제외
                        continue
                    else:cnt_2.add(k)

            ans = max(len(cnt_2),ans)

print(ans)

'''
import sys
n = int(input())
friends = [sys.stdin.readline().strip() for _ in range(n)]
ans = 0

for i in range(n):
    friends2 = set()
    for j in range(n):
        if friends[i][j] == 'N':continue
        friends2.add(j)
        for k in range(n):
            if friends[j][k] == 'N': continue
            friends2.add(k)
    ans = max(ans, len(friends2)-1)
print(ans)
'''
