from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def teacher_profile(request):
    return render(request, 'dash/admin_profile.html')
