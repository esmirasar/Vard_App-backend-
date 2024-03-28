from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('User must have an email address !!!')

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(email=email, **kwargs)

        if not password:
            raise ValueError('User must have a password !!!')

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(email, password=password, **kwargs)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_passwords_change = models.DateTimeField(null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.name:
            return self.name
        return self.email


class Place(models.Model):

    COMMUNITY = 'Community'
    MY_FILES = 'My_files'
    BEST_PRACTICES = 'Best_practices'

    CHOICES = {
        COMMUNITY: 'Community',
        MY_FILES: 'My_files',
        BEST_PRACTICES: 'Best Practices'}

    type = models.CharField(max_length=25,
                            choices=CHOICES,
                            default=COMMUNITY)

    def __str__(self):
        return self.type


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


class File(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    place = models.ForeignKey('Place', on_delete=models.CASCADE)
    type = models.ForeignKey('FileType', on_delete=models.CASCADE)

    date_creation = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(null=True, blank=True)
    date_delete = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=255)
    link = models.URLField()
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Access(models.Model):
    file = models.ForeignKey('File', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    access_type = models.ForeignKey('AccessType', on_delete=models.CASCADE)

    date_access_open = models.DateTimeField(auto_now_add=True)
    date_access_close = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.access_type} - {self.file}'


class Feedback(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    date_creation = models.DateTimeField(auto_now_add=True)
    theme = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f'({self.user}) {self.theme}: {self.description}'


class Chart(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    date_creation = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} ({self.date_creation})'


class Dashboard(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    date_creation = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} ({self.date_creation})'


class Comment(models.Model):
    file = models.ForeignKey('File', on_delete=models.CASCADE)
    chart = models.ForeignKey('Chart', on_delete=models.CASCADE)
    dashboard = models.ForeignKey('Dashboard', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    date_send = models.DateTimeField(auto_now_add=True)
    date_remove = models.DateTimeField(null=True, blank=True)
    date_delivery = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return f'{self.user}: {self.comment}'


class ReadComment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)

    date_reading = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.date_reading}'
