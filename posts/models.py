from django.db import models

# Create your models here.

class Post(models.Model):
	postID = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Publication Date')
	content = models.TextField()
	note = models.TextField(blank=True, null=True)
	def __unicode__(self):
		return self.title
