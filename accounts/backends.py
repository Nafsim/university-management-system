from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from students.models import StudentProfile


class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)

        if username is None or password is None:
            return None

        user = None
        try:
            user = UserModel.objects.get(
                Q(username__iexact=username) | Q(email__iexact=username)
            )
        except UserModel.DoesNotExist:
            try:
                profile = StudentProfile.objects.get(student_id__iexact=username)
                user = profile.user
            except StudentProfile.DoesNotExist:
                return None

        if user is not None and user.check_password(password) and self.user_can_authenticate(user):
            return user

        return None