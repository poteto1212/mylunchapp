from django.views import generic
from django.urls import reverse_lazy
from .models import Category, Shop


#一覧ページの元となるクラス
#ListViewによってモデルのページを一覧ページにする事が出来る
class IndexView(generic.ListView):
    model=Shop
    

#詳細表示の元となるクラス
#引数DetailViewはデータベースの要素別に詳細にアクセスする
class DetailView(generic.DetailView):
    model=Shop

#更新機能の元となるクラス
#CreateVieはデータモデルを作成する為のクラス
#fields="__カラムの範囲＿"　今回は全てのカラムを入力対象にしている
class CreateView(generic.edit.CreateView):
    model=Shop
    fields='__all__'

#データモデルを更新する為のクラスベースビュー
#範囲はクリエイトと同じ
class UpdateView(generic.edit.UpdateView):
    model=Shop
    fields='__all__'