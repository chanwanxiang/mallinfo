from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # 自定义用户模型类
    mobile = models.CharField(max_length=11, unique=True, verbose_name='用户的手机号')

    class Meta:
        # 自定义表名
        db_table = 'user_info'
        # 在Admin站点中可以看到中文
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    # def __str__(self):
    #     return self.username
    