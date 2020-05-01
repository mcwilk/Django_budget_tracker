from django.contrib import admin
from .models import Expense, BudgetInfo

admin.site.register(Expense)
admin.site.register(BudgetInfo)