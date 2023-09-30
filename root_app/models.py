from django.db import models

from django.urls import reverse

class Subscription(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField()
	date_added = models.DateTimeField(auto_now_add=True)
	company = models.CharField(max_length=255)

	def get_absolute_url(self):
		return reverse("subscribe_success")
