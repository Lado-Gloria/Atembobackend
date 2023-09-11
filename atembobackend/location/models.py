from django.db import models


class Location(models.Model):
    region_name = models.CharField(max_length=255)
    installation_date = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.region_name

