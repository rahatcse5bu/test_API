from django.urls import path
from CSE import views

urlpatterns = [
    path('students/', views.student_list),
    path('students/<str:roll>/', views.student_detail),
    path('ClassedBasedStudentList/', views.ClassBasedStudentList.as_view()),
    path('ClassedBasedStudentDetail/<str:roll>/', views.ClassedBasedStudentDetail.as_view()),
     path('StudentList1/', views.StudentList1.as_view()),
    path('StudentDetail1/<str:roll>/', views.StudentDetail1.as_view()),
]