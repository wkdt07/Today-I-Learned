N,K = map(int,input().split()) # N은 물품의 수, K는 버틸 수 있는 무게

things = []

for _ in range(N):
    W,V = map(int,input().split()) # 물건의 무게와 가치
    things.append((W,V))

# K까지 무게를 가지고, 최대 V를 구하는 문제

max_v = -float('inf')

