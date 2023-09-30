from django.shortcuts import render


from wagtail.models import Page
from .models import PageType

def home(request):
	context = {
		'pages': Page.objects.all(),
		'page_types': PageType.objects.all(),
	}
	template_name = 'journal/home.html'
	return render(request, template_name, context)
