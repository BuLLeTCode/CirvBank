from django.contrib import admin

# Register your models here.
from .models import Account, Transaction

admin.site.register(Account)
admin.site.register(Transaction)

class ItemAdmin(admin.ModelAdmin):
    exclude=("number",)
    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return ['number']
        return []
