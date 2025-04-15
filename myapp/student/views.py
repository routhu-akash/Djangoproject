from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student  # ← import model
from django.http import HttpResponse

def create_student(request):
    if request.method == 'POST':
        if 'cancel' in request.POST:
            return redirect('student_create')
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_create')  # redirect to refresh the form
    else:
        form = StudentForm()

    students = Student.objects.all()  # ← get all saved students
    return render(request, 'student/student_form.html', {'form': form, 'students': students})

def home(request):
    return HttpResponse("<h1>Welcome to the Student App</h1><p><a href='/student/create/'>Create Student</a></p>")
