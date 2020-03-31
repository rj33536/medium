from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class blog(models.Model):
	author = models.ForeignKey(User,on_delete = models.CASCADE, related_name="author")
	title = models.CharField(max_length = 300)
	text = models.TextField()
	created_date = models.DateTimeField(blank=True,null=True)
	publish_date = models.DateTimeField(blank = True,null = True)
	image = models.ImageField( upload_to='blog_images', blank=True)
	claps = models.ManyToManyField(User, related_name="clappers", blank=True)
	is_publish = models.BooleanField(blank=True, default=False)
	def publish(self):
		self.is_publish = True
		self.publish_date = timezone.now()
		self.save()
	def create(self):
		self.created_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.title + " " + self.text

class Comment(models.Model):
	post = models.ForeignKey(blog, on_delete=models.CASCADE, related_name='comments')
	commentator = models.ForeignKey(User,on_delete = models.CASCADE, related_name="commmentator")
	text = models.TextField()
	created_date = models.DateTimeField(blank=True,null=True)
	def __str__(self):
		return self.text

class Profile(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE, related_name="user")
	image = models.ImageField( upload_to='profile', blank=True)
