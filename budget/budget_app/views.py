from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import BudgetForm, ExpenseForm, SignupForm
from .models import BudgetInfo, Expenses


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


@login_required
def logged(request):
    return redirect('budget_list', username=request.user)


@login_required
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
    
    return render(request, 'budget_app/new_edit_budget.html', {'form': form})


@login_required
def edit_budget(request, pk):
    budget = get_object_or_404(BudgetInfo, pk=pk)
    balance = budget.balance

    if request.method == "POST":
        form = BudgetForm(request.POST, instance=budget)

        if form.is_valid():
            budget = form.save(commit=False)
            budget.owner = request.user
            budget.name = budget.name.upper()
            budget.balance += balance
            budget.save()
            return redirect('expenses', pk=pk)
    
    else:
        form = BudgetForm(instance=budget)
    
    return render(request, 'budget_app/new_edit_budget.html', {'form': form, 'budget_project': budget})


@login_required
def delete_budget(request, pk):
    budget = get_object_or_404(BudgetInfo, pk=pk)
    budget.delete()
    return redirect('budget_list', username=request.user)
    

@login_required
def budget_list(request, username):
    budgets = BudgetInfo.objects.filter(owner=request.user).order_by('-created_on')
    return render(request, 'budget_app/budget_list.html', {'budgets': budgets})


@login_required
def expenses(request, pk):
    budget = get_object_or_404(BudgetInfo, pk=pk)
    expense_list = budget.expenses.all()
    num_of_expenses = len(expense_list)
    return render(request, 'budget_app/expenses.html', {'budget_project': budget, 'expense_list': expense_list, 'num_of_expenses': num_of_expenses})


@login_required
def new_item(request, pk):
    budget = get_object_or_404(BudgetInfo, pk=pk)
    expense_list = budget.expenses.all()#[:3]
    today = timezone.now().strftime("%Y-%m-%d")

    if request.method == 'POST':
        form = ExpenseForm(request.POST)

        if form.is_valid():
            expense = form.save(commit=False)
            expense.budget = budget
            expense.title = expense.title.capitalize()
            expense.save()
            return redirect('expenses', pk=budget.pk)

    else:
        form = ExpenseForm()
    
    return render(request, 'budget_app/new_item.html', {'budget_project': budget, 'form': form, 'today': today})


@login_required
def delete_item(request, pk):
    item = get_object_or_404(Expenses, pk=pk)
    item.delete()
    return redirect('expenses', pk=item.budget.pk)


@login_required
def analysis(request, pk):
    budget = get_object_or_404(BudgetInfo, pk=pk)
    expense_list = budget.expenses.all()
    cat_amount = {}
    trans_amount = {}
    month_amount = {'January':0, 'February':0, 'March':0, 'April':0, 'May':0, 'June':0,
		    'July':0, 'August':0, 'September':0, 'October':0, 'November':0, 'December':0}

    for expense in expense_list:

        if expense.get_category_display() not in cat_amount:
            cat_amount[expense.get_category_display()] = float(expense.price)
        else:
            cat_amount[expense.get_category_display()] += float(expense.price)
    
        for m in month_amount:
            if expense.date.strftime('%B') == m:
                month_amount[m] += float(expense.price)
            else:
                continue
        
        if expense.get_transaction_display() not in trans_amount:
            trans_amount[expense.get_transaction_display()] = float(expense.price)
        else:
            trans_amount[expense.get_transaction_display()] += float(expense.price)
        
    cat_names = list(cat_amount.keys())
    cat_vals = list(cat_amount.values())
    month_names = list(month_amount.keys())
    month_vals = list(month_amount.values())
    trans_names = list(trans_amount.keys())
    trans_vals = list(trans_amount.values())

    context = {'budget_project': budget,
               'expense_list': expense_list,
               'cat_names': cat_names,
               'cat_vals': cat_vals,
               'month_names': month_names,
               'month_vals': month_vals,
               'trans_names': trans_names,
               'trans_vals': trans_vals,}

    return render(request, 'budget_app/analysis.html', context)