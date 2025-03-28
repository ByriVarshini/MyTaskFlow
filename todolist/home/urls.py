"""
URL configuration for todolist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.home,name="home"),
    path('addtask/',views.addtask,name="addtask"),
    path('viewtask/',views.viewtask,name="viewtask"),
    path('edit/<int:id>/',views.edittask,name="edittask"),
    path('delete/<int:id>/', views.deletetask, name='deletetask'),
    path('mark_as_done/<int:id>/', views.mark_as_done, name='mark_as_done'),
]
