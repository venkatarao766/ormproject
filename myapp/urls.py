from django.urls import path
from . import views

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('collage/', views.collage.as_view(), name='collage'),
    path('employee/', views.employee.as_view(), name='employee'),
    path('student/', views.student.as_view(), name='student'),
    path('university/', views.university.as_view(), name='university'),
    path('universitylist/', views.universtylist.as_view(), name='universitylist'),
    path('studentlist/', views.stdlist.as_view(), name='studentlist'),
    path('employeelist/', views.emplist.as_view(), name='employeelist'),
    path('collagelist/', views.collagelist.as_view(), name='collagelist'),
    path('thank/', views.thank, name='thank'),
]
