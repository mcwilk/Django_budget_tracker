from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logged/', views.logged, name='logged'),
    path('budgets/new', views.new_budget, name='new_budget'),
    path('budgets/<int:pk>/delete', views.delete_budget, name='delete_budget'),
    path('budgets/<username>/', views.budget_list, name='budget_list'),
    path('budgets/<int:pk>/expenses', views.expenses, name='expenses'),
    path('budgets/<int:pk>/new-item', views.new_item, name='new_item'),
    path('budgets/<int:pk>/delete-item', views.delete_item, name='delete_item'),
    path('budgets/<int:pk>/analysis', views.analysis, name='analysis'),
]