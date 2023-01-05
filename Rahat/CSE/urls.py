from django.urls import path
from CSE import views

urlpatterns = [
    path('students/', views.student_list),
    path('students/<str:roll>/', views.student_detail),

    
    path('users/', views.user_list),
    path('create_user/', views.create_user),
    path('update_user/<int:id>/', views.UserUpdate),
    path('delete_user/<int:id>/', views.delete_user),
    path('user/<int:id>/', views.user_detail),

    path('products/', views.product_list),
    path('create_product/', views.create_product),
    path('update_product/<int:id>/', views.update_product),
    path('delete_product/<int:id>/', views.delete_product),
    path('product/<int:id>/', views.single_product_detail),

    path('categories/', views.category_list),
    path('create_category/', views.create_category),
    path('update_category/<int:id>/', views.update_category),
    path('delete_category/<int:id>/', views.delete_category),
    path('category/<int:id>/', views.single_category_detail),





    path('generate_invoice/', views.generate_invoice),







    path('ClassedBasedStudentList/', views.ClassBasedStudentList.as_view()),
    path('ClassedBasedStudentDetail/<str:roll>/', views.ClassedBasedStudentDetail.as_view()),
     path('StudentList1/', views.StudentList1.as_view()),
    path('StudentDetail1/<str:roll>/', views.StudentDetail1.as_view()),
   
]