from django.shortcuts import render

def home(request):
	context = {}
	template_name = 'home.html'
	return render(request, template_name, context)

def about(request):
	context = {}
	template_name = 'about.html'
	return render(request, template_name, context)

def projects(request):
	context = {}
	template_name = 'projects.html'
	return render(request, template_name, context)