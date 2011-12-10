from django.shortcuts import get_object_or_404, render_to_response
from django.template import Context, loader
from Systems.posts.models import Post
from django.http import HttpResponse
import Systems
import ml

# Create your views here.

def index(request):
	postID = request.session.get('bookmark', 0)
	return post(request, postID)

def post(request, postID):
	postID = int(postID)
	try:
		address = Systems.settings.ROOT_URL
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
		# process mark up language
		for i in range(len(l)):
			l[i] = ml.toHTML(l[i])
		t = loader.get_template("posts/post.html")
		note = p.note.split("\n")
		has_note = p.note != ""
		c = Context({"title": p.title, "paragraphs": l, "prev": prev, "nex": nex, "addr_prefix": address, "note": note, "has_note": has_note})
		request.session["bookmark"] = postID
		return HttpResponse(t.render(c))
	except Post.DoesNotExist:
		return "404"
