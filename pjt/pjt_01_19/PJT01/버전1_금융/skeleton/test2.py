import requests
import pprint


api_key = "69c89d484a27a5510880746b8b2f56e0"
url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
   
response = requests.get(url).json()

baseList = response['result']['baseList']

optionList = response['result']['optionList']


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
        #         '금리 정보' : same_fin_data,              #same_fin_data가 o1 o2 o3에 따라 계속 재할당 되고 있다. #total을 option 밖으로 꺼내면 완료된 애만 들어가므로 데이터 사용량 줄일 수 있다. 
        #         '금융 상품명' : base['fin_prdt_nm'],
        #         '금융 회사명' : base['kor_co_nm']
        #         }
    total = {
        '금리 정보' : same_fin_data,             #total을 option 밖으로 꺼내면 완료된 total만 들어가므로 데이터 사용량 줄일 수 있다. 
        '금융 상품명' : base['fin_prdt_nm'],
        '금융 회사명' : base['kor_co_nm']
        }
    total_list.append(total)
pprint.pprint(total_list)


# pprint.pprint(baseList)
# pprint.pprint(optionList)