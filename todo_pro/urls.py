"""todo_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from todo_app import views

admin.site.site_header = "To-Do Admin"
admin.site.site_title = "To-Do Admin Portal"
admin.site.site_title = "Welcome to To-Do"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('sign',views.signup,name='sign'),
    path('logout',views.logout,name='logout'),   
    path('form',views.form,name='form'),
    path('show',views.show,name='show'),
    path('delete <int:id>',views.delete,name='delete'),
    path('update <int:id>',views.update,name='update'),
]
