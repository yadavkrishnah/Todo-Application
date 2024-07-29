"""
URL configuration for Todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from TodoApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name="home_view"),
    path('reg',views.UserRegister.as_view(),name="reg_view"),
    path('log',views.UserLoginView.as_view(),name="log_view"),
    path('logout',views.UserLogoutView.as_view(),name="logout_view"),
    path('create',views.TodoCreateView.as_view(),name="todo_create"),
    path('list',views.TodoListView.as_view(),name="todo_list"),
    path('detail/<int:id>',views.TodoDetailView.as_view(),name="todo_detail"),
    path('delete/<int:id>',views.TodoDeleteView.as_view(),name="todo_delete"),
    path('update/<int:id>',views.TodoUpdateView.as_view(),name="todo_update"),









]
