from django.shortcuts import render, redirect
from django.http import HttpResponse
from gbook.forms import EntryForm
from gbook.models import GuestbookEntry

import datetime  

# if the form is valid, it submits, and outputs the users data. It only does so for that one instance and does not save future entries. Past entries do not show up with a GET request/empty form - because entry is not defined in the else statement. 





def index(request):
	previous_entries = GuestbookEntry.objects.all().reverse()
	if request.method == "POST":
		form = EntryForm(request.POST)
		if form.is_valid():
			f_instance = form.save()

		return render(request, 'gbook/index.html', {'form': form,
						'previous_entries': previous_entries})
	else:
		form = EntryForm(request.GET)
	return render(request, 'gbook/index.html', {'form': form,
						'previous_entries': previous_entries})
	#return render(request, 'gbook/index.html', {'form': form})
'''
def entry_pages(request):
	entry_list = GuestbookEntry.objects.all().reverse()
	paginator = Paginator(entry_list, 10)

	page = request.GET.get('page')
	try:
		entries = paginator.page(page)
	except PageNotAnInteger:
		entries = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)
	return render(request, 'gbook/index.html', {'entries': entries})
		
'''














#		form = EntryForm()
#		entries = GuestbookEntry.__unicode__()
#		entries = form(instance = GuestbookEntry.objects.all().reverse())
#		return render(request, 'gbook/index.html', {'form':form})
#							'entries': entries})
'''
def entries(request):
	if request.method == "GET":
		form = EntryForm(request.GET)
		saved = GuestbookEntry.objects.all().reverse()
		saved_entries = GuestbookEntry.__unicode__(saved)		
		return render(request, 'gbook/index.html', {'form': form,
							 'saved_entries': saved_entries})










# Form shows up. Fill out. Submit. Form returned with fields filled in. 	

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




