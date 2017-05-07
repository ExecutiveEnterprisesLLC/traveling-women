from django.contrib import admin

# Register your models here.
from .models import Post, UserProfile
from django.contrib.auth.models import User

admin.site.unregister(User)

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["author", "service", "location", "comments", "timestamp"]
	list_filter = ["location", "timestamp"]
	search_fields = ["location", "service"]
	class Meta:
		model = Post

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ["user", "age", "status", "accomplice", "interests", "destinations"]
	list_filter = ["user", "age"]
	search_fields = ["user"]
	class Meta:
		model = UserProfile
			
admin.site.register(Post, PostModelAdmin)
admin.site.register(UserProfile, UserProfileAdmin)