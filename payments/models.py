from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now

User = get_user_model()

class Payment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    semester = models.IntegerField(default=1)          # Added default to avoid migration issues
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('Unpaid', 'Unpaid')
    ], default='Pending')
    
    date = models.DateField(default=now)
    invoice_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.student.username} - Sem {self.semester}"