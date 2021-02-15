from django.contrib import admin
#导入我们要注册的模型类
from learning_logs.models import Topic,Entry

#向管理网站注册模型
admin.site.register(Topic)
admin.site.register(Entry)