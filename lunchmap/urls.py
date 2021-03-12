from django.urls import path
from . import views

app_name='lunchmap'

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('create/',views.CreateView.as_view(),name='create'),
    path('<int:pk>/update/',views.UpdateView.as_view(),name='update'),
]