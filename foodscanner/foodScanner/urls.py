"""foodScanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import foodApp.views


urlpatterns = [
    path('', foodApp.views.main, name = 'gender'),
    path('main.html', foodApp.views.calculate, name = 'main'),
    path('main_man.html', foodApp.views.calculate_man, name = 'main_man'),
    path('admin/', admin.site.urls),
    path('detail/<int:detail_id>', foodApp.views.detail, name = 'detail'),
    path('detail_man/<int:detail_id>', foodApp.views.detail_man, name = 'detail_man'),

]

