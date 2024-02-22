#https://konkukcodekat.tistory.com/entry/%EB%B0%B1%EC%A4%80-11437-%EC%B5%9C%EC%86%8C-%EA%B3%B5%ED%86%B5-%EC%A1%B0%EC%83%81LCA-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EA%B8%B0%EB%B3%B8-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython


def collatz(n):
    if n%2 == 0:
        n //= 2
    else:
        n = 3*n+1
    return n
# 거꾸로 가는 이진트리 문제
a,b = map(int,input().split())
a_lst = []
b_lst = []
check = True
cnt_b = 0
while True:
    a_lst.append(a)
    b_lst.append(b)


    for a in a_lst:
        if a in b_lst:
            break


print(a_lst.index(a))
print(a)
print(b_lst.index(b))