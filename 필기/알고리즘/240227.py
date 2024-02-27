# def recursion(n):
#     if n == 6:
#         return 

#     print(n)
#     recursion(n+1)
#     print(n)
# recursion(1)

path = []
def run(n):
    if n == 3:
        print(path)
        return
    
    for i in range(1,7):
        path.append(i)
        run(n+1)
        path.pop()

run(0)