from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.forms import modelform_factory

from .models import Employee, News
from .forms import EmployeeForm


# Create your views here.

def index(request):
    news = News.objects.all().order_by('published_date')    
    return render(request, 'wsasd5/index.html', { 'news': news}) 

def employee_list(request):
    try:
        employee_list = Employee.objects.all().order_by('employee_id')
    except Employee.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'wsasd5/employee_list.html', {'employee_list': employee_list })

'''
### The codes below were only for editing purpose, since the site is like a newspaper, they are not required.


def employee_edit(request, employee_id):
    try:
        employee = get_object_or_404(Employee, employee_id = employee_id)
    except Employee.DoesNotExist:
        raise Http404("Employee does not exist")
    else:
        if request.method == 'POST':
            form = EmployeeForm(request.POST, request.FILES)
            if form.is_valid():
                employee.employee_firstname = form.cleaned_data['employee_firstname']
                employee.employee_lastname = form.cleaned_data['employee_lastname']
                employee.employee_id = form.cleaned_data['employee_id']
                employee.employee_cv = form.cleaned_data['employee_cv']
                employee.employee_photo = form.cleaned_data['employee_photo']
                employee.employee_dob = form.cleaned_data['employee_dob']
                employee.employee_position = form.cleaned_data['employee_position']
                employee.save()
                return HttpResponseRedirect(reverse('employee_list'),)
        else:
            form = EmployeeForm(initial={'employee_firstname': employee.employee_firstname, 'employee_lastname': employee.employee_lastname, 'employee_id': employee.employee_id, 'employee_photo':employee.employee_photo, 'employee_cv':employee.employee_cv, 'employee_dob': employee.employee_dob, 'employee_position':employee.employee_position})
            return render(request, 'wsasd5/employee_edit.html', {'form': form})


def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee = Employee()
            employee.employee_firstname = form.cleaned_data['employee_firstname']
            employee.employee_lastname = form.cleaned_data['employee_lastname']
            employee.employee_id = form.cleaned_data['employee_id']
            employee.employee_cv = form.cleaned_data['employee_cv']
            employee.employee_photo = form.cleaned_data['employee_photo']
            employee.employee_dob = form.cleaned_data['employee_dob']
            employee.employee_position = form.cleaned_data['employee_position']
            employee.save()
            return HttpResponseRedirect(reverse('employee_list'),)
    else:
        form = EmployeeForm()
        return render(request, 'wsasd5/employee_add.html', {'form': form})


def employee_delete(request, employee_id):
    try:
        employee = get_object_or_404(Employee, employee_id = employee_id)
        employee.delete() 
        return HttpResponseRedirect(reverse('employee_list'),)
    except Employee.DoesNotExist:
        raise Http404("Employee does not exist")




def senior_employee(request):
    employees = Employee.objects.all()
    names = []
    for i in employees:
        names.append(i.employee_firstname + ' '+ i.employee_lastname)
    return render(request, 'wsasd5/success.html', {'names':names})

def fibonacci_numbers(number):
    first_term, next_term = 1, 1
    result = []
    while number>1:
        result.append(next_term)
        first_term, next_term = next_term, first_term + next_term
        number = number-1
    if number <= 0:
        result = "Please enter a positive integer"
    return (result)

def fibonacci_gen(request):
    if request.method == "GET":
        return render(request, 'wsasd5/fibonacci_in.html')
    else:
        fibonacci_input = int(request.POST.get('fibonacci', None))
        data = {
            'fibonacci': fibonacci_numbers(fibonacci_input)
            }
        return JsonResponse(data)
'''

