from django.db import models

class Attendance(models.Model):

    student = models.ForeignKey(
        'students.StudentProfile',
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE
    )

    date = models.DateField()

    present = models.BooleanField(default=True)

    def __str__(self):
        return str(self.student)