"""
Definition of views.
"""

from django.shortcuts import render
from django.http import *
from django.template import loader
from datetime import datetime

def index(request):
    output = ""
    return HttpResponse(output)

def home(request):
    """Renders the home page."""
    context_dict = {
        'title':'Home Page', 
        'year': datetime.now().year,                   
        'message':'Your application description page.',
        'boldmessage': "I am bold font from the context"
        }
    assert isinstance(request, HttpRequest)
    return render(request, 'app\index.html', context = context_dict)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def contact(request):
    """Renders the contact page."""
    context_instance = {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    assert isinstance(request, HttpRequest)
    return render(request,'app/contact.html',context = context_instance)

def about(request):
    """Renders the about page."""
    context_instance = {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    assert isinstance(request, HttpRequest)
    return render(request,'app/about.html',context = context_instance)
