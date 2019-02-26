from django.shortcuts import render
from myapp.models import University,Collage,Employees,Student
from django.views.generic import CreateView,TemplateView,UpdateView,DeleteView,ListView

# Create your views here.
class university(CreateView):
    model = University
    fields = '__all__'
    template_name = 'university.html'
    success_url = '/thank/'

class universtylist(ListView):
    model = University
    template_name = 'unilist.html'


class collage(CreateView):
    model = Collage
    fields = ('__all__')
    template_name = 'collage.html'
    success_url = '/thank/'

class collagelist(ListView):
    model = Collage
    template_name = 'collagelist.html'

class employee(CreateView):
    model = Employees
    fields = ('__all__')
    template_name = 'employee.html'
    success_url = '/thank/'

class emplist(ListView):
    model = Employees
    template_name = 'emplist.html'


class student(CreateView):
    model = Student
    fields = ('__all__')
    template_name = 'student.html'
    success_url = '/thank/'

class stdlist(ListView):
    model = Student
    template_name = 'stdlist.html'


class home(TemplateView):
    model = Student
    template_name = 'home.html'

def thank(reqeust):
    return render(reqeust,'thank.html')
