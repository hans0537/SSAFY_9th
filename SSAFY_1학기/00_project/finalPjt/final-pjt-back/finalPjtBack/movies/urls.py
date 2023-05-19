from django.urls import path
from . import views

urlpatterns = [
    # 인기 영화
    path('',views.index),
    # 영화 상세 조회시 id는 nowmoview.json에서 정의된 id로 조회 해야 가능함
    path('<int:movie_pk>/',views.detail),
    # path('recommended/',views.recommended),
    path('<int:movie_pk>/like/',views.movielike),
    path('<int:movie_pk>/review/', views.review_create_all)
]
