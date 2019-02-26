from django.db import models

# Create your models here.
class University(models.Model):
    university_name = models.CharField(max_length=20,blank=True,null=True)
    university_id = models.PositiveIntegerField(blank=True,null=True)
    address = models.CharField(max_length=30,blank=True,null=True)
    image = models.ImageField(upload_to='media', blank=True,null=True)



    def __str__(self):
        return self.university_name

class Collage(models.Model):
    collage_name = models.CharField(max_length=30)
    collage_id = models.PositiveIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=30)
    affiliated_university = models.ForeignKey(University,on_delete=models.CASCADE)


    def __str__(self):
        return self.collage_name

class Employees(models.Model):
    employee_name = models.CharField(max_length=30)
    employee_id = models.PositiveIntegerField()
    employee_salary = models.PositiveIntegerField()
    employee_address = models.CharField(max_length=30)
    worked_at = models.ManyToManyField(Collage)

    def __str__(self):
        return self.employee_name


class Student(models.Model):
    name = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    address = models.CharField(max_length=20,blank=True,null=True)
    class_teacher = models.ForeignKey(Employees,on_delete=models.CASCADE,blank=True,null=True)
    collage = models.ForeignKey(Collage,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=10)
    date_create = models.DateField()

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=20)
    creator = models.CharField(max_length=20)
    pardigram = models.CharField(max_length=20)
    date_create = models.DateField()

    def __str__(self):
        return self.name


class Programmer(models.Model):
    name =models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    languge = models.ManyToManyField(Language)

    def __str__(self):
        return self.name

class customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Hero(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    benevolence_factor = models.PositiveSmallIntegerField(help_text="How benevolence this hero is ?",default=20)

    def __str__(self):
        return self.name