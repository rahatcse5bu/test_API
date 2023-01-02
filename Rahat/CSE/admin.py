from django.contrib import admin

# Register your models here.
#import Student model from models.py
from .models import Student
#migrate the model to admin panel
admin.site.register(Student)