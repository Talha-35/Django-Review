from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student

def home_view(request):
    # print(request.GET.get("q"))
    # print(request.COOKIES)
    # print(request.user)
    # print(request.path)
    # print(request.method)
    # return HttpResponse("HELLO. This is fscohort Home Page")
    # form = StudentForm()
    # my_context ={
    #     'title' : 'clarusway',
    #     'dict_1' : {'django' : 'best framework'},
    #     'my_list' : [2,3,4,5],
    #     'cat' : 'maviş',
    #     'form' : form
    # }
    # return render(request, "fscohort/home.html", my_context)
    return render(request, "fscohort/home.html")



def about_view(request):
    return HttpResponse("HELLO. This is fscohort About Page")




def student_list(request):
    students = Student.objects.all()
    context = {
       'students' : students,    
    }
    return render(request, "fscohort/student_list.html", context)


def student_add(request):
    form = StudentForm()
    if request.method == "POST":
        print(request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list') # işlem bittikten sonra hangi sayfaya yönlendirilmek istioyr iseniz onu yazarsıbız

    context = {
        'form': form
    }
    return render(request, "fscohort/student_add.html", context)


def student_detail(request, id):
    student = Student.objects.get(id = id)
    context = {
        'student': student
    }
    return render(request, "fscohort/student_detail.html", context)


def student_delete(request, id):
    # student = get_object_or_404(Student, id=id)
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.delete()
        return redirect("list")

    return render(request, "fscohort/student_delete.html")

def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    # student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        'student': student,
        'form': form
    }
    return render(request, "fscohort/student_update.html", context)