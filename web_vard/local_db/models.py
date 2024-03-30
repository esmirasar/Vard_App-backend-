from django.db import models

from user.models import User


class Connection(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    driver = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(max_length=255, null=True, blank=True)
    host = models.CharField(max_length=255, null=True, blank=True)
    port = models.IntegerField(null=True, blank=True)
    data_base_type = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    connection = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}: {self.description}'
