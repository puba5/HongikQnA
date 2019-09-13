from django.db import models
from datetime import datetime

# 생성한 모델은 2가지 단계, 
# 1. migration이 행해져야 하고    2. admin.py에 등록해야한다

class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__ (self):
        return self.title