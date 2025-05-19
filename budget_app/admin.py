# pylint: disable=missing-module-docstring
from django.contrib import admin

from budget_app.models import Expenses, BudgetInfo


admin.site.register(Expenses)
admin.site.register(BudgetInfo)