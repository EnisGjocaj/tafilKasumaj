from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 

# Create your views here.

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()

	form.fields["username"].widget.attrs['class'] = "fields"
	form.fields["email"].widget.attrs['class'] = "fields"
	form.fields["password1"].widget.attrs['class'] = "fields"
	form.fields["password2"].widget.attrs['class'] = "fields"


	return render(request=request, template_name="base_register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()

	form.fields["username"].label = ""
	form.fields["password"].label = ""

	form.fields["username"].widget.attrs['class'] = "login-field"
	form.fields["password"].widget.attrs['class'] = "login-field"

	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfuly logged out")
	return redirect("main:home")