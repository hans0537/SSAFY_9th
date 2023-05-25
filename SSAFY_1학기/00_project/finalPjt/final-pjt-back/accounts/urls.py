from django.urls import path
from . import views
from .views import KakaoLoginView

urlpatterns = [
    path('findUsername/', views.findUsername),
    path('findPw/', views.findPw),

    path('getUser/', views.getUser),
    
    path('update/', views.update),
    
    path('userdelete/',views.userdelete),

    path('profile/<int:user_pk>/', views.profile, name='profile'),

    path('<int:user_pk>/follow/', views.follow, name='follow'),

    path('<int:user_pk>/friends/', views.friends, name='follow'),

    path('setscore/', views.setscore),

    path('choquiz/getrank/', views.getChoRank),
    path('overview/getrank/', views.getOverviewRank),

    path('<str:game>/getmyrank/', views.getmyrank),
    path('<str:game>/getrank/<int:user_pk>/', views.getrank),

    # 소셜 로그인
    path('kakao/', KakaoLoginView.as_view())
]
