from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
import requests # 외부 url에서 데이터 받아올 수 있도록, JS의 Axios 같은 거임
# Create your views here.
from pprint import pprint
from django.conf import settings
API_KEY = settings.API_KEY
url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'

'''
class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField()
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spci_cnd = models.TextField()
    

class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts,on_delete = models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()
'''

def index(request):
    response = requests.get(url).json()
    # pass
    # result = requests.get(url)
    # baseList = result.get('baseList')
    return JsonResponse(response)

from .models import DepositProducts
from .serializers import DepositOptionsSerializer,DepositProductsSerializer
def save_deposit(request):
    result = requests.get(url).json().get('result')
    baseList = result.get('baseList')
    # print(baseList)
    for li in baseList:
        fin_prdt_cd = li.get('fin_prdt_cd')
        kor_co_nm = li.get('kor_co_nm')
        fin_prdt_nm = li.get('fin_prdt_nm')
        etc_note = li.get('etc_note')
        join_deny = li.get('join_deny')
        join_member = li.get('join_member')
        join_way = li.get('join_way')
        spci_cnd = li.get('join_way')

        data1 = {
            'fin_prdt_cd' : fin_prdt_cd,
            'kor_co_nm' : kor_co_nm,
            'fin_prdt_nm' : fin_prdt_nm,
            'etc_note' : etc_note,
            'join_deny':join_deny,
            'join_member': join_member,
            'join_way' : join_way,
            'spci_cnd' : spci_cnd,
        }    
        pdtSerializer = DepositProductsSerializer(data = data1)
        
        if DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd):
            continue
        if pdtSerializer.is_valid(raise_exception = True):
            pdtSerializer.save()
            
    optionList = result.get('optionList')
    
    for op in optionList:
        fin_prdt_cd = op.get('fin_prdt_cd')
        product = DepositProducts.objects.get(fin_prdt_cd = fin_prdt_cd)
        intr_rate_type_nm = op.get('intr_rate_type_nm')
        intr_rate = op.get('intr_rate')
        intr_rate2 = op.get('intr_rate2')
        save_trm = op.get('save_trm')
        
        data2 = {
            # 'product' : product,
            'fin_prdt_cd' : fin_prdt_cd,
            'intr_rate_type_nm' : intr_rate_type_nm,
            'intr_rate' : intr_rate,
            'intr_rate2' : intr_rate2,
            'save_trm':save_trm,
        }
        optSerializer = DepositOptionsSerializer(data = data2)
        
        
        if optSerializer.is_valid(raise_exception = True):
            optSerializer.save(product=product)
        
    return JsonResponse({'message' : 'completed!'})

from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def list_products(request):
    if request.method =="GET":
        products = DepositProducts.objects.all()
        serializers = DepositProductsSerializer(products,many = True)
        return Response(serializers.data)
    elif request.method == "POST":
        serializers = DepositProductsSerializer(data = request.data)
        if serializers.is_valid(raise_exception = True):
            serializers.save()
            return Response(serializers.data)

@api_view(['GET'])           
def option(request,fin_prdt_cd):
    products = DepositProducts.objects.filter(fin_prdt_cd = fin_prdt_cd)
    serializers = DepositProductsSerializer(products,many = True)
    return Response(serializers.data)

from .models import DepositOptions
from django.core.serializers import serialize
def top_rate(request):
    options = DepositOptions.objects.all()
    max_rate = 0
    for option in options:
        max_rate = max(max_rate,option.intr_rate2)
    # products = []
    max_options = DepositOptions.objects.filter(intr_rate2 = max_rate)
    max_option = max_options[0]
    product = DepositProducts.objects.get(fin_prdt_cd = max_option.fin_prdt_cd)
    product_data = DepositProductsSerializer(product).data
    option_data = DepositOptionsSerializer(max_option).data
    return JsonResponse({
        'Product' : product_data,
        'Option' : option_data
    })
    # print(max_options)
    # for option in max_options:
    #     product = DepositProducts.objects.get(fin_prdt_cd = option.fin_prdt_cd)
    #     products.append(product)
    # print(products)
    # serializers = DepositProductsSerializer(data = products,many = True)
    
    # if serializers.is_valid(raise_exception = True):
    #     return Response(serializers.data)
    # else:
    #     return JsonResponse({'message' : 'Failed'})
    
    # print(max_rate)

    