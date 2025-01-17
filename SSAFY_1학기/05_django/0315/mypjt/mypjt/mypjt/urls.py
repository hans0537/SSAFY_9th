"""mypjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp import views as myapp_views
from articles import views as articles_views

from myapp2 import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # path('home/', myapp_views.home),
    # path('hello/<str:name>/', articles_views.hello),
    path('articles/', include('articles.urls')),
    path('myapp/', include('myapp.urls')),

    # path('hello/<name>/', v2.hello)
    path('myapp2/', include('myapp2.urls'))
]
