from django.db import models

# Create your models here.
class ConnectedUsers(models.Model):
    first_name = models.CharField(max_length=50)
    connected = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "%s connected at %s" % (self.first_name, self.connected)