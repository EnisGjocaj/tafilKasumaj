from . import views
from django.urls import path, include

app_name = 'registration'

urlpatterns = [
    path('join/', views.register_request, name="join"),
    path('login/', views.login_request, name="login"),
    path('logout/', views.logout_request, name="logout"),
    path('', include('main.urls')),
]