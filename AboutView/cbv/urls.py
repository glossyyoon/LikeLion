from django.urls import path

from . import views

app_name = 'cbv'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'), #메인
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'), #선택지와 보트버튼
    path('<int:pk>/results/', views.ResultsView.as_view(), name = 'results'), #결과페이지
    path('<int:question_id>/vote/', views.vote, name = 'vote'), #보트
]