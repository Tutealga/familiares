from multiprocessing import context
from django.shortcuts import render

from familiares.models import Familiares

# Create your views here.
def familiares(request):
    '''familiar1 = Familiares.objects.create(name='Marta',age=54,date='31/8/1957')
    familiar2 = Familiares.objects.create(name='Juan',age=24,date='3/6/1997')
    familiar3 = Familiares.objects.create(name='Tomas',age=26,date='11/11/1995')

    context = {'familiar1':familiar1,'familiar2':familiar2,'familiar3':familiar3}'''
    
    familiares = Familiares.objects.all()

    context = {'familiares':familiares}
    
    return render(request, 'index.html', context=context)
