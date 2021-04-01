from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
# Create your views here.
def home(request):
	return HttpResponse("Home")

def calculate(request):
	if request.user.is_authenticated:
		if request.method=="POST":
			n=request.POST['value_n']
			x=request.POST['value_x']
			result=inversesum_recursion(int(n),int(x))
			result=round(result,2)
			return render(request,'home.html',{'result':result})
		else:
			return render(request,'home.html')
	else:
		return redirect('/api/login')
def inversesum_recursion(n,x):
	if n==0:
		return 0
	else:
		x=(1/(x**n))+inversesum_recursion(n-1,x)
		return x

def login1(request):
	if request.method=="POST":
		email=request.POST['email']
		password=request.POST['password']
		user=authenticate(email=email,password=password)
		if user is not None:
			login(request,user)
		else:
			return HttpResponse("Invalid Id Password")
		return redirect('/api')
	return render(request,'login.html')

