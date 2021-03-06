from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import User
class CustomUserAdmin(UserAdmin):
	add_form=CustomUserCreationForm
	form=CustomUserChangeForm
	model=User
	list_display=('email','is_staff','is_active')
	list_display=('email','is_staff','is_active')
	fieldsets=(
		(None,{'fields':('email','password','phonenumber')}),
		('Permissions',{'fields':('is_staff','is_active')}),
		)
	add_fieldsets=(
		(None,{
			'classes':('wide',),
			'fields':('email','password1','password2','phonenumber','is_staff','is_active',)}
			),
		)
	search_fields=('email',)
	ordering=('email',)
admin.site.register(User,CustomUserAdmin)
# Register your models here.
