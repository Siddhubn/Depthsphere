from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Roles available for users
    ROLE_CHOICES = (
        ('HOD', 'Head of Department'),
        ('Teacher', 'Teacher'),
        ('Student', 'Student')
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    # Override groups and user_permissions to resolve conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username
