from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from .import views
urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  
    path('register/',views.register, name="register" ),  
    path('createArticle/', views.createArticle, name="createArticle"),
    path('addComment/<int:article_id>/', views.addComment, name="addComment"),
    path('display/',views.display, name= "display"),
    path('logout/',views.logout, name= "logout"),
    #path('login/',views.login, name="login"),
]
