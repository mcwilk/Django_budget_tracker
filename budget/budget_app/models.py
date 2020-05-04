from django.db import models
from django.utils import timezone

class BudgetInfo(models.Model):
    name = models.CharField(max_length=75)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='owner')
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def balance_left(self):
        expense_list = Expense.objects.filter(budget=self)
        total_expense = 0
        for expense in expense_list:
            total_expense += expense.price
        return self.balance - total_expense
    
    def total(self):
        expense_list = Expense.objects.filter(budget=self)
        total_expense = 0
        for expense in expense_list:
            total_expense += expense.price
        return total_expense


class Expense(models.Model):
    CATEGORIES = (
        (1, "Groceries"),
        (2, "Cleaning products"),
        (3, "Cosmetics"),
        (4, "Beauty"),
        (5, "Entertainment"),
        (6, "Children"),
        (7, "Transport"),
        (8, "Education"),
        (9, "Bills"),
        (10, "Clothing"),
        (11, "Health"),
        (12, "Alcohol"),
        (13, "Cigarettes"),
        (14, "Taxes"),
        (15, "Accomodation"),
        (16, "Other"),
    )

    PAYMENT = (
        (1, "card"),
        (2, "cash"),
    )

    budget = models.ForeignKey('budget_app.BudgetInfo', on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    category = models.SmallIntegerField(choices=CATEGORIES)
    transaction = models.SmallIntegerField(choices=PAYMENT, default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date',)