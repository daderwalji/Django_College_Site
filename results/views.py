from django.shortcuts import render
from .models import Result
from .forms import result_form
from django.http import *
from django.contrib import messages
from django.db.models import Q


# Create your views here.
def resultform(request):
    if request.method=='POST':
        form = result_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/student-form/')
    else:
        form = result_form()
    return render(request,'results/studentform.html',{'form':form})

def studentresult(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = Result.objects.filter(Q(regid__iexact=srch))

            if match:
                return render(request,'results/result.html',{'sr':match})
            else:
                messages.error(request,'Enter Correct Registration ID')
        else:
            return HttpResponseRedirect('/student-result/')
    return render(request, 'results/result.html')