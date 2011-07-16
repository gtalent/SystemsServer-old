from django.shortcuts import get_object_or_404, render_to_response
from django.template import Context, loader
from posts.models import Post
from django.http import HttpResponse
import Systems

# Create your views here.

def index(request):
	return post(request, 0)

def post(request, postID):
	postID = int(postID)
	try:
		address = Systems.settings.MEDIA_URL
		p = Post.objects.get(postID=postID)
		prev = Post.objects.filter(postID=postID-1)
		if len(prev) < 1:
			prev = 0
		else:
			prev = prev[0].postID
		nex = Post.objects.filter(postID=postID+1)
		if len(nex) < 1:
			nex = postID
		else:
			nex = nex[0].postID
		l = p.content.split("\n")
		t = loader.get_template("posts/post.html")
		c = Context({"title": p.title, "paragraphs": l, "prev": prev, "nex": nex, "address": address})
		return HttpResponse(t.render(c))
	except Post.DoesNotExist:
		return "404"
