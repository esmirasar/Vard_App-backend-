from django.db import models

from file.models import File
from chart.models import Chart
from dashboard.models import Dashboard
from user.models import User


class Comment(models.Model):

    file = models.ForeignKey(File, on_delete=models.CASCADE)
    chart = models.ForeignKey(Chart, on_delete=models.CASCADE)
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    date_send = models.DateTimeField(auto_now_add=True)
    date_remove = models.DateTimeField(null=True, blank=True)
    date_delivery = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return f'{self.user}: {self.comment}'


class ReadComment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    date_reading = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.date_reading}'
