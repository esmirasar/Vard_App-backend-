from django.contrib import admin
from .models import User, Place, AccessType, FileType, File, Access, Feedback, Chart, Dashboard, Comment, ReadComment


admin.site.register(User)
admin.site.register(Place)
admin.site.register(AccessType)
admin.site.register(FileType)
admin.site.register(File)
admin.site.register(Access)
admin.site.register(Feedback)
admin.site.register(Chart)
admin.site.register(Dashboard)
admin.site.register(Comment)
admin.site.register(ReadComment)
