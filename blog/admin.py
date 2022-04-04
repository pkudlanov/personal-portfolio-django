from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple, Textarea
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
        models.TextField: {'widget': Textarea(attrs={'rows':15, 'cols':100})},
    }
    list_display = ('title', 'project', 'date', 'active',)
    list_editable = ('active',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
