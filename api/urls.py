from django.urls import path

from api import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.register),

    path('restaurants/', views.Restaurants.as_view()),
    path('dishes/', views.Dishes.as_view()),
    path('orders/', views.Orders.as_view()),


]
