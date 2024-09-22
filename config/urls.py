"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from security.views import CustomTokenObtainPairView, RegisterView, ProtectedView, AdminView

urlpatterns = [
    # JWT login and refresh token endpoints
    path('api/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # User registration endpoint
    path('api/register/', RegisterView.as_view(), name='register'),

    # Protected view
    path('api/protected/', ProtectedView.as_view(), name='protected'),
]
urlpatterns += [
    path('api/admin/', AdminView.as_view(), name='admin'),
]