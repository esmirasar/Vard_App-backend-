from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/user/', include('user.urls')),
    path('api/comment/', include('comment.urls')),
    path('api/dashboard/', include('dashboard.urls')),
    path('api/file/', include('file.urls')),
    path('api/access/', include('access.urls')),
    path('api/chart/', include('chart.urls')),
    path('api/feedback/', include('feedback.urls')),

    path('api/connection/', include('local_db.urls')),

    path(r'^auth/', include('djoser.urls')),
    path(r'^auth/', include('djoser.urls.jwt'))
]
