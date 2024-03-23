import requests
import pprint


api_key = "69c89d484a27a5510880746b8b2f56e0"
    
 
    
url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

data = requests.get(url).json()

data_option = data['result']#['optionList']
# result = []
# for dic_data in data_option:
#     result.append(dic_data)
pprint.pprint(data['result'])#['optionList']

# new_dic_list = []
# for dic in data['result']['optionList']:  
#     new_dic = {
#     '금융상품코드': dic['dcls_month'],
#     '저축 금리': dic['intr_rate'],
#     '저축 기간' : dic['save_trm'],
#     '저축금리유형' : dic['intr_rate_type'],
#     '저축금리유형명' : dic['intr_rate_type_nm'],
#     '최고 우대금리' : dic['intr_rate2'],
#     }
#     new_dic_list.append(new_dic)

# pprint.pprint(new_dic_list)

# print(key_list)
# new_key = ['저축 기간', '저축 금리','금융상품코드',  '저축금리유형', '저축금리유형명', '최고 우대금리']

# new_dic = {
#     '금융상품코드': ,
#     '저축 금리': ,
#     '저축 기간' : ,
#     '저축금리유형' : ,
#     '저축금리유형명' : ,
#     '최고 우대금리' : ,

# }

# for key in key_list:
#     for dic in data['result']['optionList']:
#         new_dic[key] = dic[key]
#         new_dic_list.append(new_dic)
# pprint.pprint(new_dic_list)
# # result = data['result']['optionList']
# # pprint.pprint(result)


# old_dic_list = []
# for dic in data['result']['optionList']:  
#     old_dic = {
#     '금융상품코드': dic['dcls_month'],
#     '저축 금리': dic['intr_rate'],
#     '저축 기간' : dic['save_trm'],
#     '저축금리유형' : dic['intr_rate_type'],
#     '저축금리유형명' : dic['intr_rate_type_nm'],
#     '최고 우대금리' : dic['intr_rate2'],
#     }'''
#     # total = {
#     # '금리정보': new_dic,
#     # '금융상품명' : '',
#     # '금융회사명' :''
#     # }'''
#     old_dic_list.append(old_dic)

# pprint(old_dic_list)


# total = {
#     '금리정보': new_dic,
#     '금융상품명' : ,
#     '금융회사명' :
# }



# data = requests.get(url).json()
# new_dic_list = []
# for dic in data['result']['optionList']:  
#     new_dic = {
#     '금융상품코드': dic['dcls_month'],
#     '저축 금리': dic['intr_rate'],
#     '저축 기간' : dic['save_trm'],
#     '저축금리유형' : dic['intr_rate_type'],
#     '저축금리유형명' : dic['intr_rate_type_nm'],
#     '최고 우대금리' : dic['intr_rate2'],
#     }
#     new_dic_list.append(new_dic)
# for i in range(len(new_dic_list)-1):
#     if new_dic_list[i+1]['금융상품코드'] == new_dic_list[i]
# pprint.pprint(new_dic_list)

# for i in range(len(new_dic_list)):
#     if new_dic



api_key = "69c89d484a27a5510880746b8b2f56e0"
url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
   
response = requests.get(url).json()

baseList = response['result']['baseList']

optionList = response['result']['optionList']


pprint.pprint(baseList)
# pprint.pprint()