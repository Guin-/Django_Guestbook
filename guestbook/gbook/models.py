from django.db import models
from django import forms
import datetime

class GuestbookEntry(models.Model):
	username = models.CharField(max_length=50)
	comment = models.TextField(max_length=500)
	user_email = models.EmailField(max_length=75, blank = True)
	timestamp = models.DateTimeField(auto_now_add = True, default = datetime.datetime.now)

	def __unicode__(self):

		return ' ---- '.join([
			self.username,
			self.comment,
			self.user_email,
		])

