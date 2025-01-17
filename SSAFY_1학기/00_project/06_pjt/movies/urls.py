from django.urls import path
from . import views


app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),


    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:movie_pk>/comments/<comment_pk>/delete', views.comments_delete, name='comments_delete'),
    path('<int:pk>/likes/', views.likes, name='likes'),

    path('<int:movie_pk>/co_comments/<int:comment_pk>/', views.co_comments_create, name='co_comments_create'),
    path('<int:movie_pk>/comments/<int:co_comment_pk>/delete/', views.co_comments_delete, name='co_comments_delete'),

    path('search/', views.search, name='search'),
]
