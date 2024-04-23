from django.urls import path

from .views import GetListConnectionAPIView, PostConnectionAPIView, ShowUserDataBaseAPIView, WorkDataBaseAPIView


urlpatterns = [
    path('', GetListConnectionAPIView.as_view()),
    path('create/', PostConnectionAPIView.as_view()),
    path('db/', ShowUserDataBaseAPIView.as_view()),
    path('db/<int:pk>/', WorkDataBaseAPIView.as_view())
]
