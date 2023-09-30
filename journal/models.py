from django.db import models

from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.search import index
from wagtail import blocks

from wagtail.fields import StreamField
from wagtail.contrib.routable_page.models import RoutablePageMixin, path

# from modelcluster.fields import ParentalKey, ParentalManyToManyField

class PageType(models.Model):
	title = models.CharField(max_length=255)

	def __str__(self):
		return self.title

class JournalPage(Page):
    body = RichTextField(blank=True)
    page_type = models.ForeignKey(PageType, on_delete=models.CASCADE)
    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]