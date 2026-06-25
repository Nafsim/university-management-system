from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from payments.models import Payment


@login_required(login_url='/login/')
def payments(request):
    if getattr(request.user, 'role', None) != 'student':
        return redirect('home')

    payments_qs = Payment.objects.filter(student=request.user).order_by('-date')
    semesters = sorted(set(payments_qs.values_list('semester', flat=True)))

    return render(request, 'student/payments.html', {
        'payments': payments_qs,
        'semesters': semesters,
        'has_payments': payments_qs.exists(),
    })
