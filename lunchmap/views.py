from django.views import generic
from django.urls import reverse_lazy
from .models import Category, Shop


#一覧ページの元となるクラス
#ListViewによってモデルのページを一覧ページにする事が出来る
class IndexView(generic.ListView):
    model=Shop
    
    
class DetailView(generic.DetailView):
    model=Shop
    
