from django.db import models

#Categoryモデル(カテゴリ名カラム　autherとの接続カラム　作成日時　更新日時)
class Category(models.Model):
    name=models.CharField(max_length=255)
     #投稿者IDからカテゴリ名にアクセス
    author=models.ForeignKey(
        'auth.user',
        on_delete=models.CASCADE,
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

#shopモデル(店名カラム　店住所カラム　投稿者IDカラム
#カテゴリidカラム)
class Shop(models.Model):
    name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    #投稿者IDからカテゴリ名にアクセス
    author=models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    #カテゴリーIDからカテゴリークラスにアクセス
    category=models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name