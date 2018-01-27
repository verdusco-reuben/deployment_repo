from django.shortcuts import render
from ..belt_app.views import *
# Create your views here.
def index(request):
	return render(request,'travel_app/index.html')
