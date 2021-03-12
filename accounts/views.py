from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

#ユーザー登録に必要となるクラス
#クラスベースの汎用ビュー
class SignUpView(generic.CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name='accounts/signup.html'
    
