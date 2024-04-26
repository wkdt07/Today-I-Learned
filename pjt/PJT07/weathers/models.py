from django.db import models

# Create your models here.


# B. DB에 저장

class Weather(models.Model):
    dt_txt = models.DateTimeField()     #관측 시간
    temp = models.FloatField()          # 온도 (기본값 : 켈빈 온도)
    feels_like = models.FloatField()    # 체감 온도 (기본값 : 켈빈 온도)