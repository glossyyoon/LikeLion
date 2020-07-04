"""gallery URL Configuration

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import  include, url
from django.conf import settings
import galleryApp.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', galleryApp.views.home, name = 'home'),
    path('createPage/', galleryApp.views.new, name = 'createPage'),
    path('create/', galleryApp.views.create, name = 'create'),
    path('update/<int:update_id>', galleryApp.views.update, name = 'update'),
    path('detail/<int:detail_id>', galleryApp.views.detail, name = 'detail'),
    path('delete/<int:delete_id>', galleryApp.views.delete, name = 'delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    



