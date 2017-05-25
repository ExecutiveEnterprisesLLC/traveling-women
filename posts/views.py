from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template

# Create your views here.
from .forms import PostForm
from .models import Post

def validateEmail( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False

def sitemap(request):
	context = {}
	return render(request, "sitemap.xml", context)

def home(request):
    context = {}
    return render(request, "home.html", context)

def refer(request):
	query = request.GET.get("email")
	if query:
		if validateEmail(query):
			send_mail('Traveling Women Talk Referal',
				get_template('refer_email.txt').render({}),
				settings.EMAIL_HOST_USER,
				[query],
				fail_silently=False)
			msg = 'Thank you for sending a referal to '+query+'! <br>Would you like to send a referal to another friend?'
		else:
			msg = 'You entered an invalid email. Please try again!'
	else:
		msg = 'Spread the word of traveling women! <br>Send an email to recommend this site to others.'
	context = {
		"title": "Refer a Friend",
		"msg": msg,
	}
	return render(request, "refer.html", context)

# def post_search(request):
# 	query = request.GET.get("q")
# 	if query:
# 		queryset = Post.objects.all().filter(location__icontains=query)
# 		context = {"object_list": queryset,}
# 	else:
# 		queryset_list = Post.objects.all()
# 		context = {"object_list": queryset_list,}
# 	return render(request, "post_search.html", context)

def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.author = User.objects.get(username=request.user)
		instance.save()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
		"title": "Create a review",
	}
	return render(request, "post_form.html", context)

def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	context = {
		"title": instance.location,
		"instance": instance,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	query = request.GET.get("q")
	if query:
		queryset_list = Post.objects.all().filter(location__icontains=query)
	else:
		queryset_list = Post.objects.all() #.order_by("-timestamp")

	paginator = Paginator(queryset_list, 10) # Show 25 posts per page

	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,
		"title": "Reviews",
		"page_request_var": page_request_var
	}
	return render(request, "post_list.html", context)

def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Item Saved")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"instance": instance,
		"title": instance.service,
		"form": form,
	}
	return render(request, "post_form.html", context)

def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("posts:list")
