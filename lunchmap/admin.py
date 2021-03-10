from django.contrib import admin
from .models import Category, Shop

#カテゴリークラスを管理サイトで有効化
admin.site.register(Category)
#ショップクラスを管理サイトで有効化
admin.site.register(Shop)
# Register your models here.
