from django.views import generic
from django.urls import reverse_lazy
from .models import Category, Shop
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
# LoginRequiredMixinを引数に含むクラスはログイン時のみアクセスできる

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
#fields対象はリスト内のみ　
class CreateView(LoginRequiredMixin,generic.edit.CreateView):
    model=Shop
    fields=['name','address','category']
    
    #ログインユーザー名を投稿者名に代入する処理を含んだ関数を定義
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)

#データモデルを更新する為のクラスベースビュー
#範囲はクリエイトと同じ
class UpdateView(LoginRequiredMixin,generic.edit.UpdateView):
    model=Shop
    fields = ['name', 'address', 'category'] # '__all__'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('You do not have permission to edit.')
        return super(UpdateView, self).dispatch(request, *args, **kwargs)
    
#データベース削除の為のクラスベースビュー
# success_url = reverse_lazy('lunchmap:index')でリダイレクト先のURLを調べる

class DeleteView(LoginRequiredMixin,generic.edit.DeleteView):
    model=Shop
    success_url = reverse_lazy('lunchmap:index')