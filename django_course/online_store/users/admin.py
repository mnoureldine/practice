from django.contrib import admin
from .models import User
from .forms import CustomUserForm

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    form = CustomUserForm

admin.site.register(User, UserAdmin)
