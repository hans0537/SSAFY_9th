from django.urls import path
from . import views

app_name = "prices"
urlpatterns = [
    path("<str:thing>/<int:cnt>/", views.price, name="price"),
]
