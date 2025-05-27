from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, UserManager

from budget_app.models import BudgetInfo, Expenses


class BudgetForm(forms.ModelForm):
    
    class Meta:
        model = BudgetInfo
        fields = ['name', 'balance']
        error_messages = {
            'name': {'required': 'Budget name is required.'},
            'balance': {'required': 'Budget balance is required.'}
        }

    def clean_balance(self):
        balance = self.cleaned_data.get('balance')

        if balance < 0:
            raise forms.ValidationError("Budget balance cannot be negative.")

        return balance

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if BudgetInfo.objects.filter(name=name.upper()).exists():
            raise forms.ValidationError(f"Budget with name {name} already exists.")
        elif len(name) < 5:
            raise forms.ValidationError("Budget name must be at least 5 characters long.")

        return name


class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expenses
        fields = ['title', 'date', 'price', 'category', 'transaction']
        #widgets = {'date': forms.DateInput()}


class SignupForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']