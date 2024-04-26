# 포장하기

from rest_framework import serializers

from .models import Weather

# form이랑 똑같음

# serializers.Serializer
    # - 모델 필드에는 없어도 추가로 변환.    
# serializers.ModelsSerializer
    # - 모델 필드에 정의된 데이터만 변환
class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'