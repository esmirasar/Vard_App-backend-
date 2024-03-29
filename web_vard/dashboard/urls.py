from django.urls import path

from .views import GetPostDashBoardAPIView, DeletePutDashboardAPIView, ListDashboardAPIView


urlpatterns = [
    path('all/', ListDashboardAPIView.as_view()),
    path('<str:my_dashboard>/', GetPostDashBoardAPIView.as_view()),
    path('<str:my_dashboard>/<int:pk>/', DeletePutDashboardAPIView.as_view())
]
