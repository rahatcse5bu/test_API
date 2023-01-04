from CSE.models import Student
from CSE.models import User
from CSE.models import Product
from CSE.models import Category
from CSE.models import Invoice
from CSE.models import Online_Payment
from CSE.models import Store
from CSE.models import Invoice_Product
from CSE.models import Notification
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        verbose_name_plural = "Categories"
class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
class Online_PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Online_Payment
        fields = '__all__'
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
class Invoice_ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice_Product
        fields = '__all__'
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
