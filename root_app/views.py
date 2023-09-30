from django.shortcuts import render

from .models import Subscription
from .forms import SubscriptionForm

from django.views.generic.edit import CreateView

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

class SubscriptionCreateView(CreateView):
    model = Subscription
    form_class = SubscriptionForm
    template_name = 'subscribe.html'

def subscribe_success(request):
	context = {}
	template_name = 'subscribe_success.html'
	return render(request, template_name, context)