from django.urls import path
from .views import login_view, home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
   
    # Excel Upload
    path('teacher/upload-excel/', views.teacher_upload_excel, name='teacher_upload_excel'),
    path('dashboard/admin/upload-excel/', views.admin_upload_excel, name='admin_upload_excel'),

    # Template Download
    path('download-excel-template/', views.download_excel_template, name='download_excel_template'),
]
