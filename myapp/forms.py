from django import forms
from myapp.models import University,Collage,Employees,Student

class Universityform(forms.ModelForm):
    class Meta():
        model = University
        fields = ('__all__')

class Collageform(forms.ModelForm):
    class Meta():
        model =Collage
        fields =('__all__')

class EmployeeForm(forms.ModelForm):
    class Meta():
        model = Employees
        fields = ('__all__')

class StudentForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = ('__all__')





