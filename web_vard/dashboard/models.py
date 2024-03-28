from django.db import models


class Dashboard(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    date_creation = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} ({self.date_creation})'
