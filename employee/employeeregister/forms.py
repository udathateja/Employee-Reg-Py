from django import forms
from .models import position
from .models import employee

class employeeForm(forms.ModelForm):
    
    class Meta:
        model = employee
        fields = ("FullName","mobile_no","emp_code","position")
        widgets={
            'FullName':forms.TextInput(attrs={'class':'form-control','id':'fullName','placeholder':'Full Name'}),
            'mobile_no':forms.TextInput(attrs={'class':'form-control','id':'mobNo','placeholder':'Mobile Number'}),
            'emp_code':forms.TextInput(attrs={'class':'form-control','id':'emp_code','placeholder':'Emp. Code'}),
            'position':forms.Select(attrs={'class':'form-control','id':'exampleFormControlSelect1'}),
        }
