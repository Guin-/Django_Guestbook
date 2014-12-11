from django.shortcuts import render
from django.http import HttpResponse
from gbook.forms import EntryForm

def index(request):
	if request.method == "POST":
		form = EntryForm(request.POST)
		if form.is_valid():
			#model_instance = form.save(commit = False)
			#model_instance.timestamp = timezone.now()
			#model_instance.save()
			return redirect('success')
		else:
			form = EntryForm()
		return render(request, 'gbook/index.html', {'form':form})

'''
from django import forms
from django.forms import ModelForm
from gbook import models as m
from gbook import forms
from gbook.forms import EntryForm
'''



'''def index(request):
	return HttpResponse("Hello Guins, you are at the Guin Guestbook Index")'''

'''def entries(request):
	page_of_entries = GuestbookEntry.objects.order_by('''




