from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple, Textarea
from .models import Post, Category, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
        models.TextField: {'widget': Textarea(attrs={'rows': 15, 'cols': 100})},
    }
    list_display = ('title', 'slug', 'project', 'date', 'active',)
    list_editable = ('active',)


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)
    list_display = ('post', 'format_date', 'name', 'email',)

    def format_date(self, obj):
        return obj.date.strftime('%d %b %Y %H:%M:%S %Z')

    format_date.admin_order_field = 'date'
    format_date.short_description = 'Date'


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
