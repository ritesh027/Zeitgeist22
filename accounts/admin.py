from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['id','email', 'username','mobile','zcode']

CustomUserAdmin.fieldsets+=('Custom fields set', {'fields': ('mobile','zcode')}),('Activation', {'fields': ('active',)}),

admin.site.register(User, CustomUserAdmin)
