from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MusicViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'music', MusicViewSet, basename='music')

urlpatterns = [
    path('', include(router.urls)),  # Include Music API endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT Token URL
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh Token URL
]

