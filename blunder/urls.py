from django.urls import path
from blunder import views


urlpatterns = [
    path('', views.LandingView.as_view(), name='index'),
    path('api/<str:page_name>', views.TestAPI.as_view(), name='api'),
    path('example/', views.ExampleView.as_view(), name='example'),
    path('profile/<str:page_name>', views.ProfileView.as_view(), name='profile_page'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('instaloader/', views.download_instagram_post, name='instaloader'),
]
