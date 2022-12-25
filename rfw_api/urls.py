
from django.contrib import admin
from django.urls import path

from rfw import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('goods/', views.create_goods),
    path('label/', views.create_label),
    path('category/', views.create_category)
]
