from django.urls import path

from . import views

app_name = 'fbv'
urlpatterns = [
    path('', views.index, name = 'index'), #메인
    path('<int:question_id>/', views.detail, name = 'detail'), #선택지와 보트버튼
    path('<int:question_id>/results/', views.results, name = 'results'), #결과페이지
    path('<int:question_id>/vote/', views.vote, name = 'vote'), #보트
]