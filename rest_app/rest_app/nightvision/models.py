from django.db import models


class Picture(models.Model):

    class Meta:
        ordering = ('created',)

    created = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField()

    def __str__(self):
        DATE_FORMAT = "%Y-%m-%d" 
        TIME_FORMAT = "%H:%M:%S"
        return self.created.strftime("%s %s" % (DATE_FORMAT, TIME_FORMAT))
