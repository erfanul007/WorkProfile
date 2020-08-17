from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.loginUser, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    path('register/',views.register, name='register'),
    path('search/',views.searchlist, name='searchlist'),
    path('<str:pk_user>/',views.profile, name='profile'),
    path('<str:pk_user>/update/',views.update, name='update')
]
