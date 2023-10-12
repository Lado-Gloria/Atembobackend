from django.db import models

class Location(models.Model):
    username = models.CharField(max_length=255, default='')  
    region_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, default='')
    installation_date = models.DateField(null=True, blank=True)
    status_choices = (
        ('Working', 'Working'),
        ('Failing', 'Failing'),
    )
    status = models.CharField(max_length=20, choices=status_choices, default='Working')
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.region_name
