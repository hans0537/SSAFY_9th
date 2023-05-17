from django.urls import path
from . import views

urlpatterns = [
    path('userdelete/',views.userdelete),
    path('profile/<username>/', views.profile, name='profile'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
