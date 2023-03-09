from django.shortcuts import render,redirect,get_object_or_404
from .forms import employeeForm
from .models import employee
from django.http import HttpResponseRedirect
# Create your views here.
def employee_list(request):
    employees=employee.objects.all()
    return render(request,'employee/employee_list.html',{'employees':employees})

def employee_form(request):
    if request.method=='POST':
        form=employeeForm(request.POST)
        if form.is_valid():
            newUser=employee(
                 FullName=request.POST['FullName'],
                 emp_code=request.POST['emp_code'],
                 mobile_no=request.POST['mobile_no'],
                 position=form.cleaned_data['position']
            
                )
            newUser.save()
            return redirect('/')
    else:
        form=employeeForm()
    context={'form':form}
    
    return render(request,'employee/employeeform.html',context)

def employee_delete(request,id):
    emp=employee.objects.get(pk=id)
    emp.delete()
    return redirect('/')

def employee_update(request,id):
    if request.method=='POST':
        pi=employee.objects.get(pk=id)
        fm=employeeForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=employee.objects.get(pk=id)
        fm=employeeForm(instance=pi)

    return render(request,'employee/employeeUpdate.html',{'form':fm})


