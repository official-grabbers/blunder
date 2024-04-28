from django.urls import path
from blunder import views


urlpatterns = [
    path('landing/', views.LandingView.as_view(), name='landing'),
    path('api/<str:page_name>', views.TestAPI.as_view(), name='api'),
    path('pagination/', views.PaginationAPI.as_view(), name='pagination'),
    path('', views.ExampleView.as_view(), name='index'),
    path('auth-view/', views.InstagramAuthView.as_view(), name='instagram_auth'),
    path('example/', views.ExampleView.as_view(), name='example'),
    path('login/', views.LoginView.as_view(), name='login'),
]
