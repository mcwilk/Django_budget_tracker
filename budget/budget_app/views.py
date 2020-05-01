from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import BudgetForm, ExpenseForm
from .models import BudgetInfo, Expense


def index(request):
    return render(request, 'budget_app/index.html', {})


def create_budget(request):

    if request.method == 'POST':
        form = BudgetForm(request.POST)

        if form.is_valid():
            budget = form.save(commit=False)
            budget.owner = request.user
            budget.save()
            return redirect('budget_list', username=request.user)
    
    else:
        form = BudgetForm()
    
    return render(request, 'budget_app/create_budget.html', {'form': form})


def budget_list(request, username):
    budgets = BudgetInfo.objects.filter(owner=request.user)
    return render(request, 'budget_app/budget_list.html', {'budgets': budgets})


# def dashboard(request, username):
#     #budget = get_object_or_404(BudgetInfo, id=)
#     expense_list = budget.expenses.all().order_by('-date')[:5]

#     if request.method == 'POST':
#         form = ExpenseForm(request.POST or None)

#         if form.is_valid():
#             form.save()
#             messages.success(request, ('Item added!'))
#             return redirect('dashboard', username=request.user)

#     else:
#         form = ExpenseForm()
    
#     return render(request, 'budget_app/dashboard.html', {'item_list': item_list, 'form': form})