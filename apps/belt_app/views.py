from django.shortcuts import render, redirect
from django.contrib import messages
from forms import LoginForm
from .models import User, Trip

# Create your views here.
def index(request):
	context = {
		'login' : LoginForm(),
		'allusers' : User.objects.all()
	}	
	return render(request, 'belt_app/index.html', context)
def register(request):
	errors =[]
	result = User.objects.register(request.POST['name'],request.POST['username'],request.POST['email'],request.POST['password'], request.POST['password_confirm'])
	if result[0]==True:
		request.session['name'] = result[1].name
		request.session['errors'] = ""
		return redirect('/travels')
	else:
		request.session['errors'] = result[1]
		return redirect('/')
def login(request):
	try:
		compare_password = request.POST['password'].encode()
		User.objects.filter(email=request.POST['email'], password=compare_password)
		login = LoginForm(request.POST)
		if login.is_valid(): 
			b = User.objects.get(email=request.POST['email'])
			request.session['name'] = b.name
			request.session['id'] = b.id
			return redirect('/travels')
	except:
		print 'hahaha!'
		return redirect('/')

def logout(request):
	request.session['errors'] = ""
	request.session['name'] = ""
	request.session['id'] = ""
	return redirect('/')
def home(request):
	try:
		context = {
			'trip' : Trip.objects.filter(plan_maker__id=request.session['id']),
			'kindame' : Trip.objects.filter(others__name=request.session['name']),
			'notme' : Trip.objects.all().exclude(plan_maker__id=request.session['id'])
			}
	except:#if they have nothing scheduled!

		context = {
			'kindame' : Trip.objects.filter(others__name=request.session['name']),
			'notme' : Trip.objects.all()
			}
	return render(request, 'belt_app/homepage.html', context)

def addtrip(request):
	return render(request, 'belt_app/addtrip.html')
def newtrip(request):
	errors =[]
	result = Trip.objects.newtrip(request.session['name'],request.POST['destination'],request.POST['desc'],request.POST['start'],request.POST['end'])
	if result[0]==True:
		return redirect('/travels')
	else:
		request.session['errors'] = result[1]
		return redirect('/books/add')
	return redirect('/books')
def userpage(request,id):
	user = Trip.objects.get(id=id)
	context = {
		'user' : user,
		'posers' : user.others.all()
	}
	return render(request, 'belt_app/finaldestination.html', context)
def join(request, id):
	Trip.objects.tag_along(id,request.session['id'])
	return redirect('/')
