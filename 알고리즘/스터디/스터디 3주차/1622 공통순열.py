'''알파벳 소문자로 이루어진 두 문자열 a와 b에 대해,
a의 부분 수열의 순열이자 b의 부분 수열의 순열이 되는 가장 긴 문자열 x를 구하여라.
'''

# 같은 알파벳을 찾아서 묶기

try:
    while True:
        a,b = input(),input()
        aset,bset = set(a),set(b)
        words = aset & bset
        result = []

        for char in words:
            cnta = a.count(char)
            cntb = b.count(char)
            result.append(char * min(cnta,cntb))
        result.sort()
        ans = ''.join(result)
        print(ans)

except:
    pass




# # 왜 틀린건지를 모르겠네...
# try:
#     while True:
#         a = input()
#         b = input()
#         lst = []
#         if len(a)>len(b):
#             for char in b:
#                 if char in a:
#                     lst.append(char)
#
#         else:
#             for char in a:
#                 if char in b:
#                     lst.append(char)
#
#         lst.sort()
#         words = ''.join(lst)
#         print(words)
# except:
#     pass