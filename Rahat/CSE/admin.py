from django.contrib import admin

# Register your models here.
#import Student model from models.py
from .models import Student
from .models import User
from .models import Store
from .models import Product
from .models import Invoice
from .models import Invoice_Product
from .models import Online_Payment
from .models import Notification
from .models import Category
#migrate the model to admin panel
admin.site.register(Student)
admin.site.register(User)
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Invoice)
admin.site.register(Invoice_Product)
admin.site.register(Online_Payment)
admin.site.register(Notification)

