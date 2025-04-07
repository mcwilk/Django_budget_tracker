from django.contrib import admin
from .models import Expenses, BudgetInfo

admin.site.register(Expenses)
admin.site.register(BudgetInfo)