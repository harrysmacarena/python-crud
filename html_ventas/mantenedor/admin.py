from django.contrib import admin

# Register your models here.

from .models import Poll,Choice,Comuna

admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Comuna)