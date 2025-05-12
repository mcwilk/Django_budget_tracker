from django.urls import path

from budget_app import views


urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logged/', views.logged, name='logged'),
    path('budgets/new', views.new_budget, name='new_budget'),
    path('budgets/<int:pk>/edit', views.edit_budget, name='edit_budget'),
    path('budgets/<int:pk>/delete', views.delete_budget, name='delete_budget'),
    path('budgets/<str:username>', views.budget_list, name='budget_list'),
    path('budgets/<int:pk>/expenses', views.expenses, name='expenses'),
    path('budgets/<int:pk>/new-item', views.new_item, name='new_item'),
    path('budgets/<int:pk>/delete-item', views.delete_item, name='delete_item'),
    path('budgets/<int:pk>/analysis', views.analysis, name='analysis'),
]