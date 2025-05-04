from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'role')  # Columns shown in list view
    fields = ('name', 'email', 'role')              # Fields shown in form (create/edit)
    search_fields = ('name', 'email', 'role')       # Optional: Enable search
