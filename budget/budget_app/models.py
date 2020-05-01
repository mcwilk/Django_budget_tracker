from django.db import models
from django.utils import timezone

class BudgetInfo(models.Model):
    name = models.CharField(max_length=75)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='owner')
    budget = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

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
        (15, "Other"),
    )

    budget = models.ForeignKey('budget_app.BudgetInfo', on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    category = models.SmallIntegerField(choices=CATEGORIES)

    def __str__(self):
        return self.title