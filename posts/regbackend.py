from registration.backends.default.views import RegistrationView
from posts.forms import UserProfileForm
from posts.models import UserProfile

class MyRegistrationView(RegistrationView):
	form_class = UserProfileForm

	def register(self, request, form_class):
		new_user = super(MyRegistrationView, self).register(form_class)
		user_profile = UserProfile()
		user_profile.user = new_user
		user_profile.age = form_class.cleaned_data['age']
		user_profile.status = form_class.cleaned_data['status']
		user_profile.accomplice = form_class.cleaned_data['accomplice']
		user_profile.interests = form_class.cleaned_data['interests']
		user_profile.destinations = form_class.cleaned_data['destinations']
		user_profile.save()
		return new_user