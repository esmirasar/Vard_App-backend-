from django.db import models


class Access(models.Model):
    file = models.ForeignKey('File', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    access_type = models.ForeignKey('AccessType', on_delete=models.CASCADE)

    date_access_open = models.DateTimeField(auto_now_add=True)
    date_access_close = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.access_type} - {self.file}'


class AccessType(models.Model):

    READER = 'Reader'
    OWNER = 'Owner'
    COMMENTATOR = 'Commentator'
    EDITOR = 'Editor'

    CHOICES = {
        READER: 'Reader',
        OWNER: 'Owner',
        COMMENTATOR: 'Commentator',
        EDITOR: 'Editor'}

    access_type = models.CharField(max_length=25,
                                   choices=CHOICES,
                                   default=READER)

    def __str__(self):
        return self.access_type