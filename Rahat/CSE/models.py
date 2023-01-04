from django.db import models
from django import forms


# Create your models here.
#create a model for the database
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.CharField(max_length=200)
    batch = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    address = models.TextField()
    blood_group = models.CharField(max_length=100)
    last_donated = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='images/', blank=True)
    cgpa= models.FloatField()
    

    def __str__(self):
        return self.name

class User(models.Model):
    id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=255,blank=False)
    role = models.CharField(max_length=255,blank=False)
    password = models.CharField(max_length=255,blank=False)
    email= models.EmailField(blank=False)
    blood_group= models.CharField(max_length=200,blank=True)
    phone = models.CharField(max_length=15,blank=False)
    joining_date=models.DateField(blank=True)
    sales_count=models.IntegerField(default=0)
    city= models.CharField(max_length=255,blank=True)
    division= models.CharField(max_length=255,blank=True)
    address= models.TextField(blank=True)
    post_code= models.CharField(max_length=255,blank=True)

    def __str__(self) -> str:
        return self.name+'( '+ self.phone +')'


class Category(models.Model):
    ID= models.AutoField(primary_key=True)
    Title=models.TextField()
    Decsription= models.TextField(blank=False)
    Image=models.TextField(blank= False)
    Parent_ID= models.ForeignKey('self',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.Title




class Product(models.Model):
    ID= models.AutoField(primary_key=True)
    Product_Title= models.TextField(blank=False)
    Product_Description=  models.TextField(blank=True)
    Product_Type=models.CharField(max_length=255,default="simple")
    Product_Image=models.TextField(blank=True)
    Product_SKU =models.CharField(max_length=255,blank=True)
    Tags= models.TextField(blank=True)
    Parent_ID=models.ForeignKey("self",on_delete=models.CASCADE)
    Stock = models.IntegerField(default=1)
    Price= models.FloatField(blank=False)
    Cat_ID= models.ForeignKey("Category",on_delete=models.CASCADE)
    User_ID = models.ForeignKey("User",on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.ID+"-"+self.Product_Title




class Store(models.Model):
    ID= models.AutoField(primary_key=True)
    Store_Name=models.TextField(blank=False)
    Store_Location= models.TextField(blank=False)
    Managers= models.TextField()
    Product_ID= models.ForeignKey("Product",on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.Store_Name


class Invoice(models.Model):
    Invoice_ID=models.AutoField(primary_key=True)
    Customer_Name =models.CharField(max_length=255,blank=False)
    Customer_Phone= models.CharField(max_length=15,blank=False)
    Customer_Email =models.EmailField(blank=True)
    Delivery_Address = models.TextField(blank=True)
    Is_Self_Delivery = models.BooleanField(default=False)
    Is_online_Payment=models.BooleanField(default=False)
    Time= models.TimeField(auto_now_add=True)
    Store_ID=models.ForeignKey("Store",on_delete=models.CASCADE)
    Sales_Manger_ID=models.ForeignKey("User",related_name="Sales_Manager_ID",on_delete=models.CASCADE)
    Store_Manager_ID= models.ForeignKey("User",related_name="Store_Manager_ID",on_delete=models.CASCADE)
    Delivery_Boy_ID= models.ForeignKey("User",related_name="Delivery_Boy_ID",on_delete=models.CASCADE)
    Delivery_Charge = models.FloatField(default=0.0)
    Product_Total_Price= models.FloatField(default=0.0)
    Discount= models.FloatField(default=0.0)
    Product_Total_Price=  models.FloatField(default=0.0)
    Remarks = models.TextField(blank=True)
    Payment_Status= models.TextField(default="Unpaid")
    Invoice_Status= models.TextField(default="Initial")

    def __str__(self) -> str:
        return self.Invoice_ID+"-"+self.Customer_Name


class Online_Payment(models.Model):
    ID=models.AutoField(primary_key=True)
    Invoice_ID= models.ForeignKey("Invoice",on_delete=models.CASCADE)
    Transaction_ID=models.CharField(max_length=255,blank=False)
    Payment_Method=models.CharField(max_length=255,blank=False)
    Amount=models.FloatField(blank=False)
    Time= models.TimeField(auto_now_add=True)
    Status=models.CharField(max_length=255,blank=False)

    def __str__(self) -> str:
        return self.Invoice_ID+"-"+self.Payment_Method+'=>'+self.Amount



class Invoice_Product(models.Model):
    ID=models.AutoField(primary_key=True)
    Invoice_ID= models.ForeignKey("Invoice",on_delete=models.CASCADE)
    Product_ID=models.ForeignKey("Product",on_delete=models.CASCADE)
    Product_Qty=models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.Invoice_ID+"-->"+self.Product_ID


class Notification(models.Model):
    ID= models.AutoField(primary_key=True)
    Sender = models.ForeignKey("User",related_name="Sender_ID",on_delete=models.CASCADE)
    Receiver=models.ForeignKey("User",related_name='Receiver_ID',on_delete=models.CASCADE)
    Message = models.TextField(blank=False)
    Time=models.TimeField(auto_now_add=True)
    Status= models.CharField(max_length=250)








