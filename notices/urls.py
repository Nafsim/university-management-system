from django.urls import path
from . import views

app_name = "notices"

urlpatterns = [

    # ==================== STUDENT ====================
    path(
        'student/notices/',
        views.student_notices,
        name='notices'
    ),

    # ==================== TEACHER ====================
    path(
        'teacher/notices/',
        views.teacher_notices,
        name='teacher_notices'
    ),

    # ==================== ADMIN ====================
    path(
        'dashboard/admin/notices/',
        views.admin_notices,
        name='admin_notices'
    ),

    path(
        'dashboard/admin/notices/add/',
        views.admin_notice_add,
        name='admin_notice_add'
    ),

    path(
        'dashboard/admin/notices/edit/<int:id>/',
        views.admin_notice_edit,
        name='admin_notice_edit'
    ),

    path(
        'dashboard/admin/notices/delete/<int:id>/',
        views.admin_notice_delete,
        name='admin_notice_delete'
    ),
]