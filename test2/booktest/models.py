from django.db import models

# Create your models here.
# 自定义管理器对象(将对象与数据库表映射)
class BookInfoManager(models.Manager):
    # 更改查询集
    def get_queryset(self):
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)
    #  在管理器中创建对象方法
    # def create(cls, btitle, bpub):
    #     b = BookInfo()
    #     b.btitle = btitle
    #     b.bpub = bpub
    #     b.bread = 0
    #     b.bcommet = 0
    #     b.isDelete = False
    #     return b

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub = models.DateField(db_column='bpub_data')
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=False)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table='bookinfo'
    books1 = models.Manager()
    books2 = BookInfoManager()
    # 创建类方法
    @classmethod
    def create(cls, btitle, bpub):
        b = BookInfo()
        b.btitle = btitle
        b.bpub = bpub
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    book=models.ForeignKey(BookInfo, on_delete=models.CASCADE)