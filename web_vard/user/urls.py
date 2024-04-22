from django.urls import path

from .views import ShowListUserAPIView, GetPutDeleteUserAPIView, PostUserAPIView, accept_registration


urlpatterns = [
    path('all/', ShowListUserAPIView.as_view()),
    path('create/', PostUserAPIView.as_view()),
    path('<str:my_profile>/', GetPutDeleteUserAPIView.as_view()),
    path('accept/<str:token>/', accept_registration)
]
