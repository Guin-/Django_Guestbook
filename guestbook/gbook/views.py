from django.shortcuts import render, redirect
from django.http import HttpResponse
from gbook.forms import EntryForm

import datetime  



def index(request):
	if request.method == "POST":
		form = EntryForm(request.POST)
		if form.is_valid():
			f_instance = form.save()
			#model_instance.timestamp = timestamp
			#model_instance.save()
		return render(request, 'gbook/index.html', {'form':form})
	else:
		form = EntryForm()
		return render(request, 'gbook/index.html', {'form':form})

def entry(request):
	if request.method == "POST" and form.is_valid():
		f_instance = form.save()
		return f_instance

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




