from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from .models import User, Question, Choice, Answer
from .forms import UserForm, LoginForm

# Create your views here.

def userform_view(request):
	if request.method == "POST":
		sform = UserForm(request.POST)
      		if sform.is_valid():
         		s=sform.save()
			return redirect('studyup/login')	
   	else:
      		sform = UserForm()
	return render(request, 'signup.html', {'form' : sform})

def loginform_view(request):
	if request.method == "POST":
		lform = LoginForm(request.POST)
      		if lform.is_valid():
			return render_to_response('home1.html')	
   	else:
      		lform = LoginForm()
	return render(request, 'login.html', {'form' : lform})

