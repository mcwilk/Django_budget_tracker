from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logged/', views.logged, name='logged'),
    path('budgets/new.', views.new_budget, name='new_budget'),
    path('budgets/<username>/', views.budget_list, name='budget_list'),
    path('budgets/<int:pk>/dashboard', views.dashboard, name='dashboard'),
]