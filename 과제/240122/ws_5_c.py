def restructure_word(word, arr):
    for a in word:
        if a.isdecimal():
            for i in range(int(a)):
                arr.pop()
        else:
            arr.remove(a)

    return arr

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []

arr.extend(original_word)
# print(arr)

result = restructure_word(word, arr)
print(''.join(result))
