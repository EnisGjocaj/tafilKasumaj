from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=200, unique=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts", editable=False)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	content = models.TextField()
	status = models.IntegerField(choices=STATUS, default=0)

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.title

class UserReport(models.Model):
	username = models.CharField(max_length=100, unique=True, blank=False)
	email = models.EmailField(max_length=100, blank=True, null=False)
	text = models.TextField()

	def __str__(self):
		return f"{self.username} ({self.email}): {self.text}"

