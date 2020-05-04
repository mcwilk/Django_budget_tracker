from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import BudgetForm, ExpenseForm, SignupForm
from .models import BudgetInfo, Expense


def index(request):
    if request.user.is_authenticated:
        return redirect('budget_list', username=request.user)
    return render(request, 'budget_app/index.html', {})


def signup(request):

    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    
    else:
        form = SignupForm()
    
    return render(request, 'registration/signup.html', {'form': form})


def logged(request):
    return redirect('budget_list', username=request.user)


def new_budget(request):

    if request.method == 'POST':
        form = BudgetForm(request.POST)

        if form.is_valid():
            budget = form.save(commit=False)
            budget.owner = request.user
            budget.name = budget.name.upper()
            budget.save()
            return redirect('budget_list', username=request.user)
    
    else:
        form = BudgetForm()
    
    return render(request, 'budget_app/new_budget.html', {'form': form})


def delete_budget(request, pk):
    budget = get_object_or_404(BudgetInfo, pk=pk)
    budget.delete()
    return redirect('budget_list', username=request.user)


def budget_list(request, username):
    budgets = BudgetInfo.objects.filter(owner=request.user).order_by('-created_on')
    return render(request, 'budget_app/budget_list.html', {'budgets': budgets})


def expenses(request, pk):
    budget = get_object_or_404(BudgetInfo, pk=pk)
    expense_list = budget.expenses.all()
    num_of_expenses = len(expense_list)
    return render(request, 'budget_app/expenses.html', {'budget': budget, 'expense_list': expense_list, 'num_of_expenses': num_of_expenses})


def new_item(request, pk):
    budget = get_object_or_404(BudgetInfo, pk=pk)
    expense_list = budget.expenses.all()#[:3]

    if request.method == 'POST':
        form = ExpenseForm(request.POST)

        if form.is_valid():
            expense = form.save(commit=False)
            expense.budget = budget
            expense.title = expense.title.capitalize()
            expense.save()
            messages.success(request, ("Product added successfully"))
            return redirect('expenses', pk=budget.pk)

    else:
        form = ExpenseForm()
    
    return render(request, 'budget_app/new_item.html', {'budget': budget, 'form': form})

def delete_item(request, pk):
    item = get_object_or_404(Expense, pk=pk)
    item.delete()
    return redirect('expenses', pk=item.budget.pk)


def analysis(request, pk):
    budget = get_object_or_404(BudgetInfo, pk=pk)
    expense_list = budget.expenses.all()
    return render(request, 'budget_app/analysis.html', {'budget': budget, 'expense_list': expense_list})