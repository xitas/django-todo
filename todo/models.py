from django.db import models

class Task(models.Model):
    option = (
        ('p', 'pending'),
        ('w', 'working'),
        ('c', 'complete'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=option, default='p')
