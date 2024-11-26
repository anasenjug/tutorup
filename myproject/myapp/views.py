# myapp/views.py

from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import StudentRegistrationForm

def index(request):
    context = {}
    return render(request, 'myapp/index.html')

def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            new_student = form.save(commit=False)
            new_student.save()
            return redirect('registration_success')
    else:
        form = StudentRegistrationForm()

    return render(request, 'myapp/register.html', {'form': form})

def registration_success(request):
    return render(request, 'myapp/registration_success.html')