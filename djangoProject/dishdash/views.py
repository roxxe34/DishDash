from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
def salam(request):
    mydict = {'insert_me': "Hello I am from views.py!"}
    return render(request, 'first_app/index.html')
