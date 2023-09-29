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

from modelcluster.fields import ParentalKey, ParentalManyToManyField


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

ARTICLE_TYPES = (
	('GI', 'General Information'),
)

class BlogPage(Page):

	body = StreamField([
		('paragraph', blocks.RichTextBlock()),
		('visualization', VisualizationLinkBlock()),
	], blank=True, use_json_field=True)

	
	visualizations = ParentalManyToManyField(Visualization)

	article_type = models.CharField(choices=ARTICLE_TYPES, max_length=255, blank=True, null=True)
	article_focus = models.CharField(max_length=255, blank=True, null=True)

	date = models.DateField("Post date")
	feed_image = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)

	# Search index configuration

	search_fields = Page.search_fields + [
		index.SearchField('body'),
		index.FilterField('date'),
	]


	# Editor panels configuration

	content_panels = Page.content_panels + [
		FieldPanel('date'),
		FieldPanel('body'),
		FieldPanel('visualizations'),
		InlinePanel('related_links', heading="Related links", label="Related link"),
	]

	promote_panels = [
		MultiFieldPanel(Page.promote_panels, "Common page configuration"),
		FieldPanel('feed_image'),
		FieldPanel('article_type'),
		FieldPanel('article_focus'),
	]


	# Parent page / subpage type rules

	# parent_page_types = ['blog.BlogIndex']
	subpage_types = []


class BlogPageRelatedLink(Orderable):
	page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='related_links')
	name = models.CharField(max_length=255)
	url = models.URLField()

	panels = [
		FieldPanel('name'),
		FieldPanel('url'),
	]

