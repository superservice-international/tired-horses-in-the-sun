from django.db import models
from django.utils import timezone
from datetime import datetime


class Picture(models.Model):

    class Meta:
        ordering = ('-created',)

    created = models.DateTimeField(blank=True)
    photo = models.ImageField()

    def save(self, *args, **kwargs):
        string_time = self.photo.name.split('.')[0]
        object_time = datetime.strptime(string_time, '%Y-%m-%d_%H-%M-%S')
        self.created = timezone.make_aware(
                object_time, timezone.get_current_timezone()
                )
        super(Picture, self).save(*args, **kwargs)


    def __str__(self):
        DATE_FORMAT = "%Y-%m-%d" 
        TIME_FORMAT = "%H:%M:%S"
        return self.created.strftime("%s %s" % (DATE_FORMAT, TIME_FORMAT))
