# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    #存储少量的文本，指定最大长度为200个字符
    date_added = models.DateTimeField(auto_now_add=True)
    #记录日期和时间参数
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    #返回存储在text中的字符串
    def __str__(self):
        """返回模型的字符串表示""" 
        return self.text

class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    #设置外键，将条目关联到每一个主题
    text = models.TextField()
    #属性text，条目不需要长度
    date_added = models.DateTimeField(auto_now_add=True)
    #按创建顺序呈现条目，并在每个条目旁放上时间戳

    #存储用于管理模型额外的信息
    class Meta:
        verbose_name_plural = 'entries'
    #返回条目前50个字符
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + "..."