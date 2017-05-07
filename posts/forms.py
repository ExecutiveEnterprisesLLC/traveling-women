from django import forms
from registration.forms import RegistrationFormUniqueEmail
from .models import Post, UserProfile
from posts.choices import *

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			'service',
			'location',
			'image',
			'comments',
		]
		labels = {
			'service': 'Hotel/Restaurant/Airline',
		}

class UserProfileForm(RegistrationFormUniqueEmail):
	age = forms.ChoiceField(label='Age',choices=AGE_CHOICES, initial='', required=True)
	status = forms.ChoiceField(label='Status',choices=STATUS_CHOICES, initial='', required=True)
	accomplice = forms.ChoiceField(label='Accomplice (pick best answer)',choices=ACCOMPLICE_CHOICES, initial='', required=True)
	interests = forms.ChoiceField(label='Interests (pick best answer)',choices=INTERESTS_CHOICES, initial='', required=True)
	destinations = forms.ChoiceField(label='Destinations (pick best answer)',choices=DESTINATION_CHOICES, initial='', required=True)