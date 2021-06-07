from django.db import models


class student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField('date published')

    def __str__(self):
        return self.first_name
