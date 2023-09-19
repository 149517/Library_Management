from django.db import models


class Book(models.Model):
    bookname = models.CharField('书名', max_length=64)
    author = models.CharField("作者", max_length=64)
    isbn = models.CharField('ISBN', unique=True, max_length=20)
    Listing_time = models.DateField("出版时间")
    updated_time = models.DateTimeField("添加时间", auto_now_add=True)
    type = models.CharField("类型", max_length=32)
    lang = models.CharField("语言", max_length=32)
    publisher = models.CharField("出版社", max_length=32)
    price = models.DecimalField("定价", max_digits=8, decimal_places=2)
    intro = models.CharField("描述", default="", max_length=512)
    # 封面来自微信读书链接，通过下载图片到服务器，通过ISBN进行索引
    pic = models.CharField("封面", default='',max_length=64)
