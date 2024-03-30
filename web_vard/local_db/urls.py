from django.urls import path

from .views import GetListConnectionAPIView, PostConnectionAPIView


urlpatterns = [
    path('', GetListConnectionAPIView.as_view()),
    path('create/', PostConnectionAPIView.as_view())
]
