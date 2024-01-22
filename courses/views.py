from django.shortcuts import render, redirect

from courses.forms import SpecialityForm
from courses.models import Subject, Speciality, Teacher


def home_page(request):
    subjects = Subject.objects.all().order_by("-created_at")[:5]
    specialities = Speciality.objects.all().order_by("-created_at")[:5]
    teachers = Teacher.objects.all().order_by("-created_at")[:5]
    context = {
        "subjects": subjects,
        "specialities": specialities,
        "teachers": teachers
    }
    return render(request, 'courses/home.html', context=context)


def teacher_detail(request, id):
    teacher = Teacher.objects.get(id=id)
    context = {
        "teacher": teacher
    }
    return render(request, 'courses/teacher_detail.html', context=context)


def speciality_detail(request, id):
    speciality = Speciality.objects.get(id=id)
    context = {
        "speciality": speciality
    }
    return render(request, 'courses/speciality_detial.html', context=context)


def speciality_create(request):
    form = SpecialityForm
    if request.method == "POST":
        form = SpecialityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:home-page')
        else:
            return render(request, "courses/speciality_create.html", context={"form": form})


    else:
        return render(request, "courses/speciality_create.html", context={"form": form})
