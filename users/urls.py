from django.urls import path
from users import views as user_views
from .apps import UsersConfig
from rest_framework_simplejwt import views


app_name = UsersConfig.name

urlpatterns = [
    # USER URLS
    path('register/', user_views.UserRegistrationView.as_view(), name='register'),

    # TOKEN URLS
    path('api/token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),

]
