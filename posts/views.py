from django.shortcuts import get_object_or_404, render_to_response
from django.template import Context, loader
from posts.models import Post
from django.http import HttpResponse

# Create your views here.

def index(request, postID):
	try:
		p = Post.objects.get(postID=postID)
		l = p.content.split("\n")
		t = loader.get_template("posts/post.html")
		c = Context({"title": p.title, "paragraphs": l})
		return HttpResponse(t.render(c))
	except Post.DoesNotExist:
		return "404"
