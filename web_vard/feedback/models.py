from django.db import models

class Feedback(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    date_creation = models.DateTimeField(auto_now_add=True)
    theme = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f'({self.user}) {self.theme}: {self.description}'
