from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView

# Create your views here.
# def home(request):
# 	return HttpResponse("Ek no")

class HomeView(TemplateView):
	# template_name ='admins/homepage/adminhome.html'
	template_name = 'users/index.html'