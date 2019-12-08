from django.shortcuts import render
from cells.models import arrow

# Create your views here. 

def Index(request):
	arrows = arrow.objects.all()
	return render(request,"dashboard/index.html",{"arrows": arrows,"title":"Dashboard"})
def map(request):
    return render(request, "dashboard/map.html")
    
