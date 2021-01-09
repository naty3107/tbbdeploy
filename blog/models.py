from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
import datetime

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

# Create your models here.

class DateCreateModMixin(models.Model):
	class Meta:
		abstract = True

	created_date = models.DateTimeField(default=timezone.now())
	mod_date = models.DateTimeField(blank=True, null=True)


class Post(DateCreateModMixin):

	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=40, default=slugify(title))

	def save(self, *args, **kwargs):
		if not self.id:
			# Newly created object, so set slug
			#self.slug = slugify(self.title)

			super(Post, self).save(*args, **kwargs)

	body = MarkdownxField()
	background_image = models.ImageField(default='img/header.jpg', upload_to=timezone.now().strftime('backgrounds/%Y/%m/%d'))

	# Note: background_image is just for my header background, not MarkdownX

	def __str__(self):
		return self.title

	def formatted_markdown(self):
		return markdownify(self.body)

	def body_summary(self):
		return markdownify(self.body[:300] + "...")
