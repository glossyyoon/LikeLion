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

    path('form/',foodApp.views.form, name = 'form'),
    path('form1/',foodApp.views.form1, name = 'form1'),

    path('detail/<int:detail_id>', foodApp.views.detail, name = 'detail'),
    path('detail1/<int:detail_id>', foodApp.views.detail1, name = 'detail1'),
    path('detail2/<int:detail_id>', foodApp.views.detail2, name = 'detail2'),
    path('detail3/<int:detail_id>', foodApp.views.detail3, name = 'detail3'),
    path('detail4/<int:detail_id>', foodApp.views.detail4, name = 'detail4'),
    path('detail5/<int:detail_id>', foodApp.views.detail5, name = 'detail5'),
    path('detail6/<int:detail_id>', foodApp.views.detail6, name = 'detail6'),

    path('detail_man/<int:detail_id>', foodApp.views.detailman, name = 'detailman'),
    path('detail_man1/<int:detail_id>', foodApp.views.detailman1, name = 'detailman1'),
    path('detail_man2/<int:detail_id>', foodApp.views.detailman2, name = 'detailman2'),
    path('detail_man3/<int:detail_id>', foodApp.views.detailman3, name = 'detailman3'),
    path('detail_man4/<int:detail_id>', foodApp.views.detailman4, name = 'detailman4'),
    path('detail_man5/<int:detail_id>', foodApp.views.detailman5, name = 'detailman5'),
    path('detail_man6/<int:detail_id>', foodApp.views.detailman6, name = 'detailman6'),
]

