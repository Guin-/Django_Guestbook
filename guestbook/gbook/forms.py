from django.db import models
from django.forms import ModelForm
from gbook.models import GuestbookEntry
 
class EntryForm(ModelForm):
	class Meta:
		model = GuestbookEntry  
		fields = ['username', 'comment', 'user_email']



