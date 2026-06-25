from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from accounts import views as account_views

urlpatterns = [
    # Home & Auth
    path('', account_views.home, name='home'),
    path('login/', account_views.login_view, name='login'),
    path('logout/', account_views.logout_view, name='logout'),

    # Django Admin
    path('admin/', admin.site.urls),

    # ==================== APPS ====================
    path('payments/', include('payments.urls', namespace='payments')),
    path('notices/', include('notices.urls', namespace='notices')),

    # ==================== TEACHER URLS ====================
    path('dashboard/teacher/', account_views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher/courses/', account_views.teacher_courses, name='teacher_courses'),
    path('teacher/students/', account_views.teacher_students, name='teacher_students'),
    path('teacher/student/<int:student_id>/', account_views.student_details, name='student_details'),
    path('teacher/upload-marks/', account_views.teacher_upload_marks, name='teacher_upload_marks'),
    path('teacher/results/', account_views.teacher_results, name='teacher_results'),
    path('teacher/upload-excel/', account_views.teacher_upload_excel, name='teacher_upload_excel'),

    # ==================== STUDENT URLS ====================
    path('dashboard/student/', account_views.student_dashboard, name='student_dashboard'),
    path('student/courses/', account_views.student_courses, name='student_courses'),
    path('student/results/', account_views.student_results, name='student_results'),
    path('student/profile/', account_views.student_profile, name='student_profile'),

    # ==================== ADMIN URLS ====================
    path('dashboard/admin/', account_views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/admin/students/', account_views.admin_students, name='admin_students'),
    path('dashboard/admin/teachers/', account_views.admin_teachers, name='admin_teachers'),
    path('dashboard/admin/courses/', account_views.admin_courses, name='admin_courses'),
    path('dashboard/admin/results/', account_views.admin_results, name='admin_results'),
    path('dashboard/admin/payments/', account_views.admin_payments, name='admin_payments'),
    
    # Marks Upload
    path('dashboard/admin/upload-marks/', account_views.admin_upload_marks, name='admin_upload_marks'),
    path('dashboard/admin/upload-excel/', account_views.admin_upload_excel, name='admin_upload_excel'),
    path('download-excel-template/', account_views.download_excel_template, name='download_excel_template'),

    # Course Assignment
    path('dashboard/admin/assign-course/', account_views.assign_course, name='assign_course'),
    path('dashboard/admin/assign-course-student/', account_views.assign_course_student, name='assign_course_student'),

    # Student CRUD
    path('dashboard/admin/student/add/', account_views.admin_student_add, name='admin_student_add'),
    path('dashboard/admin/student/edit/<int:id>/', account_views.admin_student_edit, name='admin_student_edit'),
    path('dashboard/admin/student/delete/<int:id>/', account_views.admin_student_delete, name='admin_student_delete'),
    path('dashboard/admin/student/<int:student_id>/details/', account_views.admin_student_details, name='admin_student_details'),
    path('dashboard/admin/student/<int:student_id>/payment/add/', account_views.admin_payment_add, name='admin_payment_add'),
    path('dashboard/admin/payment/add/', account_views.admin_payment_add_direct, name='admin_payment_add_direct'),
    path('dashboard/admin/payment/edit/<int:payment_id>/', account_views.admin_payment_edit, name='admin_payment_edit'),
    path('dashboard/admin/payment/delete/<int:payment_id>/', account_views.admin_payment_delete, name='admin_payment_delete'),

    # Teacher CRUD
    path('dashboard/admin/teacher/add/', account_views.admin_teacher_add, name='admin_teacher_add'),
    path('dashboard/admin/teacher/edit/<int:id>/', account_views.admin_teacher_edit, name='admin_teacher_edit'),
    path('dashboard/admin/teacher/delete/<int:id>/', account_views.admin_teacher_delete, name='admin_teacher_delete'),
    path('dashboard/admin/teacher/<int:id>/details/', account_views.admin_teacher_details, name='admin_teacher_details'),

    # Course CRUD
    path('dashboard/admin/course/add/', account_views.admin_course_add, name='admin_course_add'),
    path('dashboard/admin/course/edit/<int:id>/', account_views.admin_course_edit, name='admin_course_edit'),
    path('dashboard/admin/course/delete/<int:id>/', account_views.admin_course_delete, name='admin_course_delete'),

    # Notices
    path('dashboard/admin/notices/', account_views.admin_notices, name='admin_notices'),
    path('dashboard/admin/notices/add/', account_views.admin_notice_add, name='admin_notice_add'),
    path('dashboard/admin/notices/edit/<int:id>/', account_views.admin_notice_edit, name='admin_notice_edit'),
    path('dashboard/admin/notices/delete/<int:id>/', account_views.admin_notice_delete, name='admin_notice_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)