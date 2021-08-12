from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from .models import Project, Tag


class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)
