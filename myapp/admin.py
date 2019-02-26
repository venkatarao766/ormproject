from django.contrib import admin
from .models import Student,Company,Programmer,Language,customer,Category,Hero,University,Collage,Employees
# Register your models here.
# class Studentdata(admin.ModelAdmin):
#     list_display = ['id','name','email']
class universitydetail(admin.ModelAdmin):
    list_display = ['id','university_id','university_name','address']
admin.site.register(University,universitydetail)

class collagedetails(admin.ModelAdmin):
    list_display = ['id','collage_name','collage_id','address','email','affiliated_university']
admin.site.register(Collage,collagedetails)

class employeedetails(admin.ModelAdmin):
    list_display = ['id','employee_id','employee_salary','employee_address']
admin.site.register(Employees,employeedetails)

class studentdetails(admin.ModelAdmin):
    list_display = ['id','name','email','address','class_teacher','collage']
admin.site.register(Student,studentdetails)


admin.site.register(Company)
admin.site.register(Programmer)
admin.site.register(Language)
admin.site.register(customer)
admin.site.register(Category)
admin.site.register(Hero)



