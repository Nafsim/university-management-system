from django.db import models
from django.conf import settings
from courses.models import Course


class Result(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='results'
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.PositiveIntegerField(default=1)

    quiz_marks = models.FloatField(default=0)
    forum_marks = models.FloatField(default=0)
    assignment_marks = models.FloatField(default=0)
    midterm_marks = models.FloatField(default=0)
    final_marks = models.FloatField(default=0)

    marks = models.FloatField(default=0)
    grade = models.CharField(max_length=10, blank=True)
    gpa = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('student', 'course', 'semester')
        ordering = ['-semester', 'course']

    def save(self, *args, **kwargs):
        self.marks = (
            self.quiz_marks +
            self.forum_marks +
            self.assignment_marks +
            self.midterm_marks +
            self.final_marks
        )

        total = self.marks

        if total >= 80:
            self.grade, self.gpa = "A+", 4.00
        elif total >= 75:
            self.grade, self.gpa = "A", 3.75
        elif total >= 70:
            self.grade, self.gpa = "A-", 3.50
        elif total >= 65:
            self.grade, self.gpa = "B+", 3.25
        elif total >= 60:
            self.grade, self.gpa = "B", 3.00
        elif total >= 55:
            self.grade, self.gpa = "B-", 2.75
        elif total >= 50:
            self.grade, self.gpa = "C+", 2.50
        elif total >= 45:
            self.grade, self.gpa = "C", 2.25
        elif total >= 40:
            self.grade, self.gpa = "D", 2.00
        else:
            self.grade, self.gpa = "F", 0.00

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.username} - {self.course.course_code} (Sem {self.semester})"