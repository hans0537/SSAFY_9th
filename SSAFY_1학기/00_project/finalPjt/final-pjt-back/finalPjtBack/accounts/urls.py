from django.urls import path
from . import views

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
    path('overview/getrank/', views.getOverviewRank)
]
