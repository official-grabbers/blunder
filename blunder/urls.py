from django.urls import path
from blunder import views


urlpatterns = [
    path('', views.ExampleView.as_view(), name='example'),
]
