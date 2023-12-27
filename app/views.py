from django.shortcuts import render

from django.http import HttpResponse

from app.models import *


# Create your views here.



def foms(request):
    if request.method=='POST':

        username=request.POST['un']
        password=request.POST['pw']

        un=data.objects.get_or_create(un=username,pw=password)[0]
        un.save()


    return render(request,'foms.html')

