from django.shortcuts import render, redirect
from django.http import HttpResponse
from gbook.forms import EntryForm
from gbook.models import GuestbookEntry

import datetime  

# if the form is valid, it submits, and outputs the users data. It only does so for that one instance and does not save future entries. Past entries do not show up with a GET request/empty form - because entry is not defined in the else statement. 





def index(request):
	if request.method == "POST":
		form = EntryForm(request.POST)
		if form.is_valid():
			f_instance = form.save()
			entry = GuestbookEntry.__unicode__(f_instance)		
		#	return render(request, 'gbook/index.html',
		#				 {'entry': entry, 
		#				  'form': form})
			#model_instance.timestamp = timestamp
			#model_instance.save()
		return render(request, 'gbook/index.html', {'form': form,
							'entry': entry})
	else:
		form = EntryForm()
#		entries = GuestbookEntry.__unicode__(self)
		entries = GuestbookEntry.objects.all()
		return render(request, 'gbook/index.html', {'form':form,
							'entries': entries})



# Form shows up. Fill out. Submit. Form returned with fields filled in. 	
'''
def index(request):
	if request.method == "POST":
		form = EntryForm(request.POST)
		if form.is_valid():
			#f_instance = form.save()
			#model_instance.timestamp = timestamp
			#model_instance.save()
			return render(request, 'gbook/index.html', {'form':form})

'''


# return form data on same index.html template below the display of the form

'''def index(request):
	return HttpResponse("Hello Guins, you are at the Guin Guestbook Index")'''

'''def entries(request):
	page_of_entries = GuestbookEntry.objects.order_by('''




