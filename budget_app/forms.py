from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BudgetInfo, Expenses


class BudgetForm(forms.ModelForm):
    
    class Meta:
        model = BudgetInfo
        fields = ['name', 'balance']


class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expenses
        fields = ['title', 'date', 'price', 'category', 'transaction']
        #widgets = {'date': forms.DateInput()}


class SignupForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']