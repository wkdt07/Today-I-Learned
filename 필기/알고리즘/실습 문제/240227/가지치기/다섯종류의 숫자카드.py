cards = list(map(int,input()))

def pr(ans=[],cur = 0):
    global cnt

    if len(ans)>=2 and abs(ans[-1]-ans[-2]) >3:
        return


    if cur == 4:
        cnt += 1
        return


    for card in cards:
        ans.append(card)
        pr(ans,cur+1)
        ans.pop()

cnt = 0
pr()
print(cnt)