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
    path('generate_invoice/', views.generate_invoice),

    path('ClassedBasedStudentList/', views.ClassBasedStudentList.as_view()),
    path('ClassedBasedStudentDetail/<str:roll>/', views.ClassedBasedStudentDetail.as_view()),
     path('StudentList1/', views.StudentList1.as_view()),
    path('StudentDetail1/<str:roll>/', views.StudentDetail1.as_view()),
   
]