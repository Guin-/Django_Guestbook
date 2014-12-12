from django.shortcuts import render, redirect
from django.http import HttpResponse
from gbook.forms import EntryForm

def index(request):
	if request.method == "POST":
		if form.is_valid():
			form = EntryForm(request.POST)
		
		#model_instance = form.save(commit = False)
		#model_instance.timestamp = timezone.now()
		#model_instance.save()
		return render(request, '/gbook/index.html', {'form':form})
	else:
		form = EntryForm()
		return render(request, 'gbook/index.html', {'form':form})







# return form data on same index.html template below the display of the form

'''def index(request):
	return HttpResponse("Hello Guins, you are at the Guin Guestbook Index")'''

'''def entries(request):
	page_of_entries = GuestbookEntry.objects.order_by('''




