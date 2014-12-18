from django.contrib import admin
from mails.models import EmailContent

class EmailContentAdmin(admin.ModelAdmin):
    search_fields = ["name", "slug"]
    list_display = ('name', 'subject', 'slug',)
    prepopulated_fields = {'slug': ('name',)}
    class Media:
        js = (
            "/static/js/tinymce/tinymce.min.js",
            "/static/js/tinymce.js",
            )
admin.site.register(EmailContent, EmailContentAdmin)
