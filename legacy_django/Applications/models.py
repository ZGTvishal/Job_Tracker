from django.db import models
from django.utils import timezone

# Create your models here.

class Application(models.Model):
    sender_email = models.EmailField(max_length=255)
    sender_name = models.CharField(max_length=255)
    company_domain = models.TextField(blank=True, null=True)
    role_title = models.CharField(max_length=255, blank=True, null= True, default='Software Engineer')
    
    first_seen_date = models.DateTimeField(default=timezone.now)
    last_update_date = models.DateTimeField()

    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interview', 'Interview'),
        ('rejected', 'Rejected'),
        ('offer', 'Offer'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')

    class Meta:
        unique_together = ('company_domain', 'role_title')

    def __str__(self):
        return f"{self.company_domain} | {self.role_title} | {self.status}"

