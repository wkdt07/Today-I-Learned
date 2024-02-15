import heapq

q = []

heapq.heappush(q,8)
heapq.heappush(q,4)
heapq.heappush(q,7)
heapq.heappush(q,3)
heapq.heappush(q,1) # 우선순위가 높은 애를 맨 앞으로

print(q) #[1,3,4,7] #[1,3,7,8,4

ans1 = heapq.heappop(q)
ans2 = heapq.heappop(q)
ans3 = heapq.heappop(q)
ans4 = heapq.heappop(q)


print(ans1) #1
print(ans2) #3
print(ans3) #4
print(ans4) #7
