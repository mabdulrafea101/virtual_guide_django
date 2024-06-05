from django.db import models

# Create your models here.


class UniversityLocation(models.Model):

    class Meta:
        app_label = "website"
        db_table = ''
        managed = True
        verbose_name = 'University Location'
        verbose_name_plural = 'University Locations'

    location_name = models.CharField(max_length=100, blank=True)
    location_frame = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.location_name
