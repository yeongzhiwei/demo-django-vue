from django.contrib import admin

from expense.models import Expense, Tag


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    radio_fields = {"status": admin.HORIZONTAL}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
