from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect 
from rest_framework import viewsets
from .models import Routes
from .serializer import AllRoutesSerializer
from django.contrib import messages
from .forms import ContactForm
# Create your views here.


def home(request):
	if request.method =='POST':
		email = request.POST['email']
		message = request.POST['message']
		return redirect('home.html', {
			'email': email,
			'message': message,
			})
	else:
		return render(request, 'home.html')

class AllRoutes(viewsets.ModelViewSet):
	queryset = Routes.objects.all()
	serializer_class = AllRoutesSerializer
	http_method_names = ['get']

