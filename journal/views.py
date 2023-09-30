from django.shortcuts import render


from wagtail.models import Page

def home(request):
	context = {
		'pages': Page.objects.all()
	}
	template_name = 'journal/home.html'
	return render(request, template_name, context)
