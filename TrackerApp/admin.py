from django.contrib import admin

from .models import Project, Label, Task, Activity

#register models
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Activity)
admin.site.register(Label)
