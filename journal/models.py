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

"""
class Visualization(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	code = models.TextField()
	
	def __str__(self):
		return self.title

class VisualizationLinkBlock(blocks.StructBlock):
	href = blocks.CharBlock(required=True)
	text = blocks.CharBlock(required=True)
	id_ = blocks.CharBlock(required=True)
	float_ = blocks.CharBlock(required=True)

	class Meta:
		template = 'visualization_link_block.html'
"""
ARTICLE_TYPES = (
	('GI', 'General Information'),
)

class JournalPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]