from Systems.posts.models import Post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'postID')
	fieldsets = [(None, {'fields': ['postID', 'title', 'pub_date', 'content', 'note']})]

admin.site.register(Post, PostAdmin)
