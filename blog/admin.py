from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
