from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Notice


@login_required
def admin_notices(request):
    notices = Notice.objects.all().order_by('-created_at')
    return render(request, 'admin/notices.html', {'notices': notices})


@login_required
def admin_notice_add(request):
    if request.method == "POST":
        Notice.objects.create(
            title=request.POST.get('title'),
            message=request.POST.get('message'),
            created_by=request.user
        )
        return redirect('admin_notices')

    return render(request, 'admin/notice_form.html')


@login_required
def admin_notice_edit(request, id):
    notice = get_object_or_404(Notice, id=id)

    if request.method == "POST":
        notice.title = request.POST.get('title')
        notice.message = request.POST.get('message')
        notice.save()
        return redirect('admin_notices')

    return render(request, 'admin/notice_form.html', {
        'notice': notice
    })


@login_required
def admin_notice_delete(request, id):
    notice = get_object_or_404(Notice, id=id)
    notice.delete()
    return redirect('admin_notices')



@login_required
def student_notices(request):
    notices = Notice.objects.all().order_by('-created_at')

    return render(
        request,
        'student/student_notices.html',
        {
            'notices': notices
        }
    )


@login_required
def teacher_notices(request):
    notices = Notice.objects.all().order_by('-created_at')

    return render(
        request,
        'teacher/teacher_notices.html',
        {'notices': notices}
    )