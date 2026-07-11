from django.shortcuts import render, redirect, get_object_or_404
from .models import Department, Student


# -------------------------
# Home
# -------------------------

def home(request):
    return render(request, "home.html")


# -------------------------
# Department Views
# -------------------------

def department_list(request):
    departments = Department.objects.all()
    return render(request, "department/department_list.html", {
        "departments": departments
    })


def department_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            Department.objects.create(name=name)
            return redirect("department_list")

    return render(request, "department/department_create.html")


def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            department.name = name
            department.save()
            return redirect("department_list")

    return render(request, "department/department_update.html", {
        "department": department
    })


def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        department.delete()
        return redirect("department_list")

    return render(request, "department/department_delete.html", {
        "department": department
    })


# -------------------------
# Student Views
# -------------------------

def student_list(request):
    students = Student.objects.select_related("department").all()

    return render(request, "student/student_list.html", {
        "students": students
    })


def student_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        department_id = request.POST.get("department")

        if name and age and email and department_id:
            department = get_object_or_404(Department, pk=department_id)
            Student.objects.create(
                name=name,
                age=age,
                email=email,
                department=department
            )
            # print(student.id)
            # print(student.name)
            # print(student.department.id)
            # print(student.department.name)
            return redirect("student_list")

    departments = Department.objects.all()
    print(departments)
    return render(request, "student/student_create.html", {
        "departments": departments
    })


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        department_id = request.POST.get("department")

        if name and age and email and department_id:
            department = get_object_or_404(Department, pk=department_id)
            student.name = name
            student.age = age
            student.email = email
            student.department = department
            student.save()
            return redirect("student_list")

    departments = Department.objects.all()
    return render(request, "student/student_update.html", {
        "student": student,
        "departments": departments
    })


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.delete()
        return redirect("student_list")

    return render(request, "student/student_delete.html", {
        "student": student
    })