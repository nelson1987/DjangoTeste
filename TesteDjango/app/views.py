"""
Definition of views.
"""

from django.shortcuts import render
from django.http import *
from django.template import loader
from datetime import datetime

def home(request):
    """Renders the home page."""
    context_dict = {
        'title':'Home Page', 
        'year': datetime.now().year,                   
        'message':'Your application description page.',
        'boldmessage': "I am bold font from the context"}
    return render(request, 'app\index.html', context = context_dict)
    #return render(request, 'app\index.html', context_dict)
    #assert isinstance(request, HttpRequest)
    #template = loader.get_template('app/WebPage1.html')
    # context = {
    #        'title':'Home Page',
    #        'year':datetime.now().year,
    #        'contexto': [1,2,4,6,8]
    #    }
    #return render(request,'app/WebPage1.html',context)
    #    request,
    #    'app/index.html',
    #    context = context
    #)
    #return HttpResponse("Hello, world.  You're at the polls index.")
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }))

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }))
