from django.shortcuts import render, redirect
from django.http import HttpResponse
from gbook.forms import EntryForm
from gbook.models import GuestbookEntry
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime  


	
def index(request):
	
	entry_list = GuestbookEntry.objects.order_by('-timestamp')

	paginator = Paginator(entry_list, 10)
        
	page = request.GET.get('page')

	try:
		entries = paginator.page(page)
	except PageNotAnInteger:
		entries = paginator.page(1)
	except EmptyPage:
		entries = paginator.page(paginator.num_pages)

	if request.method == "POST":
		form = EntryForm(request.POST)
		if form.is_valid():
			f_instance = form.save()

	else:
		form = EntryForm()
	return render(request, 'gbook/index.html', {'form': form,
						'entries': entries})












