from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Profile)
admin.site.register(BugReport)
admin.site.register(Workplace)
admin.site.register(TaskTracker)
