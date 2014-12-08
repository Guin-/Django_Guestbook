from django import forms
from gbook import models

class EntryForm(forms.ModelForm):
	class Meta:
		model = GuestbookEntry


