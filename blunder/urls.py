from django.urls import path
from blunder import views


urlpatterns = [
    path('', views.ExampleView.as_view(), name='example'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('instaloader/', views.download_instagram_post, name='instaloader'),
]
