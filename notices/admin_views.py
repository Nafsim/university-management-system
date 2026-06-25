from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Notice


@login_required(login_url='/login/')
def admin_notices(request):
    notices = Notice.objects.all().order_by('-created_at')
    return render(request, 'admin/notices.html', {'notices': notices})


@login_required(login_url='/login/')
def admin_notice_add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        message = request.POST.get("message")

        Notice.objects.create(
            title=title,
            message=message,
            created_by=request.user
        )

        messages.success(request, "Notice created successfully")
        return redirect('admin_notices')

    return render(request, 'admin/notice_form.html')


@login_required(login_url='/login/')
def admin_notice_edit(request, id):
    notice = get_object_or_404(Notice, id=id)

    if request.method == "POST":
        notice.title = request.POST.get("title")
        notice.message = request.POST.get("message")
        notice.save()

        messages.success(request, "Notice updated")
        return redirect('admin_notices')

    return render(request, 'admin/notice_form.html', {'notice': notice})


@login_required(login_url='/login/')
def admin_notice_delete(request, id):
    notice = get_object_or_404(Notice, id=id)
    notice.delete()
    messages.success(request, "Notice deleted")
    return redirect('admin_notices')