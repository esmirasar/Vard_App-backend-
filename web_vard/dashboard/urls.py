from django.urls import path

from .views import GetPostDashBoardAPIView, DeletePutDashboardAPIView


urlpatterns = [
    path('', GetPostDashBoardAPIView.as_view()),
    path('<int:pk>/', DeletePutDashboardAPIView.as_view())
]
