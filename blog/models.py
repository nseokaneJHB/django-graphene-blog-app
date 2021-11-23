from django.db import models
from accounts.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils.text import slugify


# Create your models here.
class LikeModel(models.Model):
	author = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.author)

	@receiver(post_save, sender=CustomUser)
	def create_like_author(sender, instance, created, **kwargs):
		if created:
			LikeModel.objects.create(author=instance)


class BlogModel(models.Model):
	author = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
	title = models.CharField(max_length=255, unique=True) 
	body = models.TextField()
	likes = models.ManyToManyField(LikeModel, blank=True)
	meta_description = models.CharField(max_length=150, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	published = models.BooleanField(default=False)
	publish_date = models.DateTimeField(blank=True, null=True)
	slug = models.SlugField(max_length=255, unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(f'{self.title}')
		super().save(*args, **kwargs)

	def __str__(self):
		return str(f"Blog: {self.title}")

	class Meta:
		ordering = ['-date_created']
	
	
class CommentModel(models.Model):
	author = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
	post = models.ForeignKey(BlogModel, on_delete=models.PROTECT)
	comment = models.TextField()
	likes = models.ManyToManyField(LikeModel, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(f"Comment by Name: {self.author}")

	class Meta:
		ordering = ['-date_created']