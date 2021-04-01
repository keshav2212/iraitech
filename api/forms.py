from .models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		models=User
		fields=('email','phonenumber')
class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model=User
		fields=('email','phonenumber')