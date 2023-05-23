from django.urls import path
from . import views

urlpatterns = [
    # 전체영화 조회
    path('',views.index),
    # 현재 상영작 조회
    path('nowmovie/', views.nowmovie),
    # 인기영화 조회
    path('popularmovie/',views.popularmovie),
    # 상영 예정작 조회
    path('upcommovie/',views.upcommovie),
    # 영화 상세 조회시 정의된 id로 조회 해야 가능함
    path('<int:movie_pk>/',views.detail),
    # path('recommended/',views.recommended),
    path('<int:movie_pk>/like/',views.movielike),
    path('<int:movie_pk>/review/', views.review_create_all),
    path('<int:movie_pk>/review/<int:comment_pk>/', views.comment_update_del, name='comment_update_del'),
]
