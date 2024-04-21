from django.urls import path
from blunder import views


urlpatterns = [
    path('', views.ExampleView.as_view(), name='example'),
    path('instaloader/', views.download_instagram_post, name='instaloader'),
]
