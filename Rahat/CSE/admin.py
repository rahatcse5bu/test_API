from django.contrib import admin

# Register your models here.
#import Student model from models.py
from .models import Student
from .models import User
from .models import Store
from .models import Product
from .models import Category
#migrate the model to admin panel
admin.site.register(Student)
admin.site.register(User)
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Category)