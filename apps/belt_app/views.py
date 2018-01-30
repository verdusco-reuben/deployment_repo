from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Trip

# Create your views here.
def index(request):
	context = {
		'allusers' : User.objects.all()
	}	
	return render(request, 'belt_app/index.html', context)

def register(request):
	if request.path == '/login':
		result = User.objects.login(request.POST['username'],request.POST['password'])
	else:
		result = User.objects.register(request.POST['name'],request.POST['username'],request.POST['password'], request.POST['password_confirm'])
	if result[0]==True:
		request.session['name'] = result[1].name
		request.session['id'] = result[1].id
		return redirect('/travels')
	else:
		request.session['errors'] = result[1]
	return redirect('/')
def logout(request):
	request.session.flush()
	return redirect('/')
def home(request):
	return render(request, 'belt_app/homepage.html', Trip.objects.homepage(request.session['id']))
def addtrip(request):
	return render(request, 'belt_app/addtrip.html')
def newtrip(request):
	result = Trip.objects.newtrip(request.session['id'],request.POST['destination'],request.POST['desc'],request.POST['start'],request.POST['end'])
	if result[0]==True:
		return redirect('/travels')
	else:
		request.session['errors'] = result[1]
		return redirect('/travels/add')
def destination(request,id):
	context = Trip.objects.destination(id,request.session['id'])
	return render(request, 'belt_app/finaldestination.html', context)
def join(request, id):
	Trip.objects.tag_along(id,request.session['id'])
	return redirect('/travels')