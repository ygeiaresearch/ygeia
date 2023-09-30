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

def page_type(request, page_type):
	pages = Page.objects.filter(journalpage__page_type__title=page_type)
	context = {
		'pages': pages,
		'page_type': page_type
	}
	template_name = 'journal/page_type.html'
	return render(request, template_name, context)