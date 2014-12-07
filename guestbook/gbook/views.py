from django.shortcuts import render

# Create your views here.



from django.http import HttpResponse

# Views are controllers in a traditional MVC pattern
# A URLconf maps url patterns to views

# Gbook needs an index view - that will display the main page (form and previous entries)
# This will map the index template to the url so that it is displayed. 

# Each view is defined by a function. It is defined by a method if using class based views. 

def index(request):
	return HttpResponse("Hello Guin's, you are at the Guin Guestbook Index")
