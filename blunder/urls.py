from django.urls import path
from blunder import views
from blunder.constants import SubRoutes


# api_patterns = [
#     path('landing/', views.LandingView.as_view(), name='landing'),
#     path('api/<str:page_name>', views.TestAPI.as_view(), name='api'),
#     path('pagination/', views.PaginationAPI.as_view(), name='pagination'),
#     path('', views.ExampleView.as_view(), name='index'),
#     path('auth-view/', views.InstagramAuthView.as_view(), name='instagram_auth'),
#     path('business-auth-view/', views.FacebookAuthView.as_view(), name='facebook_auth'),
#     path('example/', views.ExampleView.as_view(), name='example'),
#     path('login/', views.LoginView.as_view(), name='login'),
# ]

urlpatterns = [
    # path(RouteGroups.API_ROUTES, include(api_patterns)),
    path(SubRoutes.ROOT, views.IndexView.as_view(), name="index"),
    path('static/tailwind', views.FileRenderer.as_view(), name="get_file_from_firebase"),
]
