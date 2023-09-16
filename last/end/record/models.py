from django.db import models


class Record(models.Model):
    user = models.ForeignKey('user.UserInfo', on_delete=models.CASCADE)
    # 使用ForeignKey关联User模型中的id字段
    type = models.CharField("记录类型", max_length=12)
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE, unique=True)
    status = models.BooleanField("状态", default=True)
    addTime = models.DateTimeField("添加时间", auto_now_add=True)
