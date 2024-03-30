from django.db import models

from user.models import User


class FileType(models.Model):

    CSV = 'CSV'
    JSON = 'JSON'
    EXCEL = 'EXCEL'
    PDF = 'PDF'
    OTHER = 'Other'

    CHOICES = {
        CSV: 'CSV',
        JSON: 'JSON',
        EXCEL: 'EXCEL',
        PDF: 'PDF',
        OTHER: 'Other'
    }

    files_type = models.CharField(max_length=25,
                                  choices=CHOICES,
                                  default=OTHER)

    def __str__(self):
        return self.files_type


class Place(models.Model):

    COMMUNITY = 'Community'
    MY_FILES = 'My_files'
    BEST_PRACTICES = 'Best_practices'

    CHOICES = {
        COMMUNITY: 'Community',
        MY_FILES: 'My_files',
        BEST_PRACTICES: 'Best Practices'
    }

    type = models.CharField(max_length=25,
                            choices=CHOICES,
                            default=COMMUNITY)

    def __str__(self):
        return self.type


class File(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    type = models.ForeignKey(FileType, on_delete=models.CASCADE)

    date_creation = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(null=True, blank=True)
    date_delete = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=255)
    link = models.FilePathField(null=True, blank=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.name
