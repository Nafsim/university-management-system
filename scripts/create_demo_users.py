from django.contrib.auth import get_user_model
User = get_user_model()

for email, role in [('student@example.com','student'),('teacher@example.com','teacher'),('admin@example.com','admin')]:
    try:
        u = User.objects.get(email=email)
    except User.DoesNotExist:
        uname = email.split('@')[0]
        orig = uname
        i = 1
        while User.objects.filter(username=uname).exists():
            uname = f"{orig}{i}"
            i += 1
        u = User.objects.create_user(username=uname, email=email, password='12345')
    u.set_password('12345')
    u.role = role
    u.save()

print('demo users ready')
