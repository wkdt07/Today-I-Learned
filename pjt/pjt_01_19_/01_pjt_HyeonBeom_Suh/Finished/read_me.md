# Prob 1

  구현까지는 굉장히 간단했다. 
    사실 URL만 찾아서 작성한다면 20초도 걸리지 않았을 것이다.
  문제는, 처음 보는 형태이고, 처음으로 진행하는 pjt이다보니 익숙치 않음이 어렵다 생각하게 된 계기가 됐다. 단순히 딕셔너리의 키를 출력해야한다는 점만 고민했다면 내장함수를 알고 있으니 간단하게 해결됐겠지만, 처음으로 진행하는 프로젝트인만큼 익숙치 않음이 문제였다.

  # prob 2

  개인적으로 4개의 문제 중 가장 간단한 문제였다. 내장함수를 따로 사용할 필요도 없고, 단순히 키를 이용해 접근하는 내용만 이해한다면 됐다고 생각한다. 

  # prob 3

  먼저, 가장 크게 배웠던 것은 dictionary의 키를 변경하는 방법이다. 마치 tuple의 값을 변경하기 위해 매개되는 값을 이용하는 것처럼, dictionary를 새로 작성하여 이 dict에 추가하므로서 데이터 값들을 갖고 나와서 키를 변경하는 방법에 대해서 배웠다. 
  사실 어제 실습 문제를 완전히 풀지 못했는데, 이를 이용해서 풀릴 것이라 예상한다.
  또한 함수의 매개변수에 대해서도 다시 학습했는데, 로컬과 글로벌과 인클로져의 범위 내에서 변수를 재지정하므로서 이에 대한 이해를 늘릴 수 있었다.

  # prob 4

오후 시간 내내 이 문제를 위해 매달렸다. 배웠던 내용이자 가장 여려웠던 내용은(사실 아직 완전히 알진하겠다.) for문, 특히 2중 for문에서 append 등으로 값을 추가할 때, 어느 시점에서 이를 작성해야하는지이다. 아래는 그에 대한 예시이다. 

```python
    
    total_list=[]
    for base in baseList:
        same_fin_data = []
        for option in optionList:
            if base['fin_prdt_cd'] == option['fin_prdt_cd']:
                fin_data_dic = {
                '저축 금리': option['intr_rate'],
                '저축 기간' : option['save_trm'],
                '저축금리유형' : option['intr_rate_type'],
                '저축금리유형명' : option['intr_rate_type_nm'],
                '최고 우대금리' : option['intr_rate2']
                }
                same_fin_data.append(fin_data_dic)
            
            # else:
            #     continue
        
            # total = {
            #         '금리 정보' : same_fin_data,              #same_fin_data가 o1 o2 o3에 따라 계속 재할당 되고 있다.
            #         '금융 상품명' : base['fin_prdt_nm'],
            #         '금융 회사명' : base['kor_co_nm']
            #         }
        total = {
            '금리 정보' : same_fin_data,             #total을 option 밖으로 꺼내면 완료된 total만 들어가므로 데이터 사용량 줄일 수 있다. 
            '금융 상품명' : base['fin_prdt_nm'],
            '금융 회사명' : base['kor_co_nm']
            }
        total_list.append(total)
    
```

여기서 total이 들어가야 할 자리, total_list가 들어가야 할 자리, for option과 for base 중 뭐가먼저 나와야 하는 지 등을 고민하는 것이 굉장히 어려웠다. 손코딩으로 하나하나 값을 넣어가면서 생각해보면서 이러한 부분이 좀 개선되긴 하였지만, 아직 갈 길이 멀다 생각했다.
또한 굳이 2중 for 문을 활용해야 하는 점이 굉장히 아쉽다. 물론 base의 요소와 option의 요소를 같이 비교하려면 이는 어쩔 수 없는 상황이었지만, 좀 더 고민해보면 이를 사용하지 않고도 코드를 작성하고, 나아가 좀 더 직관적으로 코드를 짤 수 있지 않았을까 생각한다.  

