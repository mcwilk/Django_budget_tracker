from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', include('budget_app.urls')),
]
