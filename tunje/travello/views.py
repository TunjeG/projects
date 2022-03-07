from django.shortcuts import render

from .models import Facilities

# Create your views here.
def index(request):

    facilits = Facilities.objects.all()




    return render(request, "index.html", {'facilits': facilits})