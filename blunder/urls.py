from django.urls import path
from blunder import views


urlpatterns = [
    path('', views.LandingView.as_view(), name='index'),
    path('api/<str:page_name>', views.TestAPI.as_view(), name='api'),
    path('pagination/', views.PaginationAPI.as_view(), name='pagination'),
    path('example/', views.ExampleView.as_view(), name='example'),
    path('login/', views.LoginView.as_view(), name='login'),
]
