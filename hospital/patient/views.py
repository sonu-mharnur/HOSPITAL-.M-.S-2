from django.shortcuts import render
from .forms import hospitalForm

# Create your views here.

def registerhospital(request):
    if request.POST:
        pass
    form = hospitalForm()
    return render(request,'hospitalregister.html',{'form':form})

