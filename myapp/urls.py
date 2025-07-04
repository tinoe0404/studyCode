from django.urls import path
from . import views

urlpatterns = [
   path('login/', views.loginPage, name="login"),
   path('logout/', views.user_logout, name="logout"), 
   path('register/', views.registerUser, name="register"),
   path('', views.home, name= "home"),
   path('room/<str:pk>/', views.room, name= "room"),
   path('profile/<str:pk>/', views.userProfile, name="userProfile"),
   path('create-room/', views.createRoom, name="create-room"),
   path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
   path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
   path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
   path('update_user/', views.updateUser, name="update_user"),

   
]