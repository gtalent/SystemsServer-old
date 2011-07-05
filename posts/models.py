from django.db import models

# Create your models here.

class Post(models.Model):
	postID = models.IntegerField()
	title = models.CharField(max_length=200)
	content = models.TextField()
	def __unicode__(self):
		return self.title
