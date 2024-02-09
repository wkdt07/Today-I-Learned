# import sys
#
# diff = [6*i for i in range(31)]
#
# for deg in sys.stdin.readlines():
#     if int(deg) in diff:
#         print('Y')
#     else:
#         print('N')

import sys

diff = [6*i for i in range(31)]

for deg in sys.stdin.readlines():
    if int(deg)%6 ==0:
        print('Y')
    else:
        print('N')