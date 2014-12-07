from django.db import models

# Create your models here.

# A table called GuestbookEntry
# This table will have 3 fields:
# 1. Name 2. Email 3. Comment
# Name and Comment fields are required. 
# Email should be validated as actual email address. 

class GuestbookEntry(models.Model):
	username = models.CharField(max_length=50)
	# TextField uses the default form widget: Text area. Max_length will be displayed in the widget, but not enforced at the database level. 
	comment = models.TextField(max_length=500)
	#EmailField verifies that it is an email, blank allows it to be optional
	user_email = models.EmailField(max_length=75, blank = True)






