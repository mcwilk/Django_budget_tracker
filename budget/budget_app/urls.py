from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('budgets/<username>/', views.budget_list, name='budget_list'),
]