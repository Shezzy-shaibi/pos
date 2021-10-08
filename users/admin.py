from allauth.account.models import EmailAddress
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ['pk','email', 'username', 'first_name','is_superuser' ]

    # search list
    search_fields = ['first_name', 'last_name', 'username',  'email']

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('email','first_name','last_name','address1','address2','zip_code','city','country','mobile_phone','recharged_amount')}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('address1','address2','zip_code','city','country','mobile_phone','recharged_amount')}),

    )

admin.site.register(CustomUser, CustomUserAdmin)
