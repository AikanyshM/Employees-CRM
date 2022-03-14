from unicodedata import category
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Branch, Employee
from django.urls import reverse

def welcome(request):
    return HttpResponse("Welcome to our company!")

def form(request):
    return render(request, 'form.html')

def employees_view(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def detail_view(request, id):
    single_emp = Employee.objects.get(id=id)
    return render(request, 'single_emp.html', {'single_emp': single_emp})

def delete_view(request, id):
    delete_emp = Employee.objects.get(id=id)
    delete_emp.delete()
    # return redirect(reverse("all_employees"))
    return HttpResponse("Запись удалена")

def create_view(request):
    if request.method == "GET":
        branches = Branch.objects.all()
        return render(request, 'create_emp.html', {'branches': branches})
    
    if request.method == "POST":
        name = request.POST.get("name")
        position = request.POST.get("position")
        branch_id = request.POST.get("branch")
        birthdate = request.POST.get("birthdate")
        employment_date = request.POST.get("employment_date")
        
        branch=Branch.objects.get(id=branch_id)

        new_employee = Employee(
            first_last_name=name, 
            position=position,
            branch=branch,
            birthdate=birthdate,
            employment_date=employment_date, 
            )
        new_employee.save()

        return redirect(reverse("all_employees"))


def update_view(request, id):
    single_emp = Employee.objects.get(id=id)
    if request.method == "GET":
        branches = Branch.objects.all()
        context = {
            'branches': branches,
            'single_emp': single_emp
        }
        return render(request, 'update_emp.html', context)

    if request.method == "POST":
        name = request.POST.get("name")
        position = request.POST.get("position")
        branch_id = request.POST.get("branch")
        birthdate = request.POST.get("birthdate")
        employment_date = request.POST.get("employment_date")
        
        branch=Branch.objects.get(id=branch_id)

        single_emp.first_last_name = name
        single_emp.position = position
        single_emp.branch = branch
        single_emp.birthdate = birthdate
        single_emp.employment_date = employment_date
        single_emp.save()


        return redirect(reverse("all_employees"))

    





