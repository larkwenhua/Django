from django.db import models

# Create your models here.
class Bookinfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub = models.DateField()
    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    # 添加on_delete参数
    hbook = models.ForeignKey('Bookinfo', on_delete=models.CASCADE)
    def __str__(self):
        return self.hname


