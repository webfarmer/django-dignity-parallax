from django.contrib import admin
from django.http import HttpResponseRedirect
from models import BlockContent, Page, ParallaxConfig, Contact


class ParallaxConfigAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
       try:
           location = '/admin/parallax/parallaxconfig/%d' % ParallaxConfig.objects.get_or_create(id=1, defaults={})[0].id
           return HttpResponseRedirect(location)
       except:
           return super(ParallaxConfigAdmin, self).changelist_view(request, extra_context)

admin.site.register(ParallaxConfig, ParallaxConfigAdmin)

class BlockContentAdmin(admin.ModelAdmin):
    model = BlockContent
    list_display = ["slug", "display"]
    list_editable = ('display',)
    list_filter = ('display',)
    fieldsets = (
        (None, {
            'fields': (('display','slug',),'content',),
        }),
    )
    class Media:
        js = (
            "/static/js/tinymce/tinymce.min.js",
            "/static/js/tinymce.js",
        )
admin.site.register(BlockContent, BlockContentAdmin)

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']
    list_display = ('title', 'slug', 'display')
    list_filter = ('display',)
    list_editable = ('display','slug',)
    fieldsets = (
        (None, {
            'fields': (('display','title','slug',),'content',),
            }),
        ("Meta Details", {
            'classes': ('collapse',),
            'fields': (('meta_title', 'meta_description', 'meta_keywords',),)
        }),
    )

    class Media:
        js = (
            "/static/js/tinymce/tinymce.min.js",
            "/static/js/tinymce.js",
        )
admin.site.register(Page, PageAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email','contact_number',)
admin.site.register(Contact, ContactAdmin)
