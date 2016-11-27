"""
Definition of views.
"""

from django.shortcuts import render
from django.http import *
from django.template import loader
from datetime import datetime
import motor.motor_tornado

def index(request):
    output = ""
    return HttpResponse(output)

def home(request):
    """Renders the home page."""
    client = motor.motor_tornado.MotorClient('mongodb://appharbor_c5d7wkq2:his526rhtr0i2tttfagho6quk@ds111718.mlab.com:11718/appharbor_c5d7wkq2')
    db = client['test_database']
    #while row:
    #    print str(row[0]) + " " + str(row[1]) + " " + str(row[2])   
    #    row = cursor.fetchone()
    tabela = []
    cursor = db.usuarios().find({'i': {'$lt': 5}})
    while (yield cursor.fetch_next):
        document = cursor.next_object()
        tabela.append(document)

    context_dict = {
        'title':'Home Page', 
        'year': datetime.now().year,                   
        'message':'Your application description page.',
        'boldmessage': "I am bold font from the context",
        'table': tabela
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
