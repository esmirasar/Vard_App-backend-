from django.urls import path, include

from .views import GetPostDashBoardAPIView, DeletePutDashboardAPIView


urlpatterns = [
    path('', GetPostDashBoardAPIView.as_view()),
    path('<int:pk>/', DeletePutDashboardAPIView.as_view())
]
