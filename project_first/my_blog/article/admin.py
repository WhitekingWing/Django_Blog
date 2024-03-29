from django.contrib import admin
from .models import ArticlePost
# Register your models here.
#注册ArticlePost到admin中
from .models import ArticleColumn

# 注册文章栏目
admin.site.register(ArticleColumn)
admin.site.register(ArticlePost)
