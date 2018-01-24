from django.shortcuts import render, redirect
from forms import UserForm, LoginForm
from .models import User, Book, Review

# Create your views here.
def index(request):
	if request.path == "/submitform":
		print 'this works!'
		form = UserForm(request.POST)
		if form.is_valid():
			request.session['name'] = request.POST['name']
			form.save()
			return redirect('/books')
		else:
			return redirect('/')
	
	elif request.path == '/login':
		print 'that works!'
		login = LoginForm(request.POST)
		if login.is_valid(): 
			b = User.objects.get(email=request.POST['email'])
			request.session['name'] = b.name
			return redirect('/books')
		else:
			print 'hahaha!'
			return redirect('/')
	
	context = {
		'form' : UserForm(),
		'login' : LoginForm(),
		'all' : User.objects.all()
	}	

	return render(request, 'belt_app/index.html', context)

def startpage(request):
	if request.path == '/logout':
		request.session['name'] = ''
	return redirect('/')
def home(request):
	context = {
		'books' : Book.objects.all(),
		'reviews' : Review.objects.get(book=Book.objects.get(id=1)),
	}
	return render(request,'belt_app/books.html', context)
def singlebook(request, id):
	book = Book.objects.get(id=id)
	review = Review.objects.get(book=Book.objects.get(id=id))
	context = {
		'book' : book,
		'reviews' : review  
	}
	return render(request,'belt_app/bookprofile.html', context)
# if User.objects.filter(email=request.POST['email'], password=request.POST['password'])==[] or login.is_valid()== False:
	