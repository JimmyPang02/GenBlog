"""
URL configuration for GenBlogAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from account_manager.views import get_user_list, follow_user, unfollow_user, show_followers, update_user_info, \
    get_current_user_info
from article_manager.views import create_article, show_articles, show_articles_by_id
from get_jwt.views import get_jwt_token, validate_access_jwt, validate_refresh_jwt
from login.views import login
from register.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', register, name='register'),
    path('api/login/', login, name='login'),
    path('api/get_jwt_token/', get_jwt_token, name='get_jwt_token'),
    path('api/get_user_list/<int:page_begin>/<int:page_end>/', get_user_list, name='get_user_list'),
    path('api/validate_access_jwt/', validate_access_jwt, name='validate_access_jwt'),
    path('api/validate_refresh_jwt/', validate_refresh_jwt, name='validate_refresh_jwt'),
    path('api/follow_user/', follow_user, name='follow_user'),
    path('api/unfollow_user/', unfollow_user, name='unfollow_user'),
    path('api/show_followers/', show_followers, name='show_followers'),
    path('api/create_article/', create_article, name='create_article'),
    path('api/show_articles/', show_articles, name='show_articles'),
    path('api/show_articles_by_id/', show_articles_by_id, name='show_articles_by_id'),
    path('api/update_user_info/', update_user_info, name='update_user_info'),
    path('api/get_current_user_info/', get_current_user_info, name='get_current_user_info'),
]
