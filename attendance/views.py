from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class RoleLoginView(LoginView):

    template_name = 'login/login.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['role'] = self.request.GET.get(
            'role',
            'student'
        )

        return context

    def get_success_url(self):

        user = self.request.user

        if user.role == 'student':
            return reverse_lazy(
                'student_dashboard'
            )

        elif user.role == 'teacher':
            return reverse_lazy(
                'teacher_dashboard'
            )

        elif user.role == 'admin':
            return reverse_lazy(
                'admin_dashboard'
            )

        return '/'