from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django import forms
from django.forms import ModelForm
from gbook import models as m
# Views are controllers in a traditional MVC pattern
# A URLconf maps url patterns to views

# Gbook needs an index view - that will display the main page (form and previous entries)
# This will map the index template to the url so that it is displayed. 
# Each view is defined by a function. It is defined by a method if using class based views. 

'''def index(request):
	return HttpResponse("Hello Guin's, you are at the Guin Guestbook Index")'''

'''def entries(request):
	page_of_entries = GuestbookEntry.objects.order_by('''



# instantiate a form class within a view. Use POST method. 
# use a django ModelForm to generate a form directly from gbookentry model. 
# from gbook import models as m
# from django.forms import ModelForm

'''class EntryForm(forms.Form):
	user_name = forms.CharField(max_length=50)
	comment = forms.CharField(max_length=500)
	user_email = forms.EmailField(max_length=75)'''


'''class EntryForm(forms.ModelForm):
	class Meta:
		model = m.GuestbookEntry
		fields = ('username', 'comment', 'user_email')'''
