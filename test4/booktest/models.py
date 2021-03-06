from django.db import models

# Create your models here.

class Bookinfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub = models.DateField(db_column='bpub_data')
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=False)
    isDelete = models.BooleanField(default=False)
    class Meta():
        db_table = 'bookinfo'


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    book=models.ForeignKey('BookInfo',on_delete=models.CASCADE)
    def showname(self):
        return self.hname