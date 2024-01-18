list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_book = [
    '장생전',
    '위대한 개츠비',
    '원생몽유록',
    '이생규장전',
    '데미안',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]

missing_book = [rental_book[i] for i in range(len(rental_book)) if rental_book[i] not in list_of_book]

#  이거 set으로 차집합 써도 되겠다.

# missing_book = list(set(rental_book)-set(list_of_book))


for miss in missing_book:
    print(f'{miss} 을/를 보충해야합니다.')


