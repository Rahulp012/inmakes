
from django.shortcuts import render
from . models import place
from . models import emp


def demo1(request):
   obj=place.objects.all()
   ob=emp.objects.all()

   return render(request,"index.html",{'result':obj,'res':ob})




