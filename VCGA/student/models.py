from django.db import models

# Create your models here.


class ParticipatedEvent(models.Model):
    participant = models.ForeignKey(
        "user.CustomUser", 
        related_name="event", 
        on_delete=models.CASCADE)
    event = models.ForeignKey(
        'university.Event',
        related_name='participated', 
        on_delete=models.CASCADE)
    is_participated = True

    def __str__(self):
        pass

    class Meta:
        app_label = 'student'
        db_table = ''
        managed = True
        verbose_name = 'Participated Event'
        verbose_name_plural = 'Participated Events'