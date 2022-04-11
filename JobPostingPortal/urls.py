"""JobPostingPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from User.views import Jobs_Page, home, login_page, register_page
from User.urls import User_router

urlpatterns = [
    path('jobs/', Jobs_Page, name="addjob"),
    path('', home, name="home"),
    path('admin/', admin.site.urls),
    path('register/', register_page, name="register"),
    path('nogin/', login_page, name="login"),
]

urlpatterns += [
    path('partone/', include(User_router.urls))
]
