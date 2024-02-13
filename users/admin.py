from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.forms import SelectDateWidget
from .models import User

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        widgets = {
            'fecha_nacimiento': SelectDateWidget(years=range(1900, 2023)),
        }

class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    list_filter = ('is_staff',)

admin.site.register(User, CustomUserAdmin)
