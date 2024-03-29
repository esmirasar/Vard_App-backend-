from django.contrib import admin

from .models import Access, AccessType


admin.site.register(Access)
admin.site.register(AccessType)
