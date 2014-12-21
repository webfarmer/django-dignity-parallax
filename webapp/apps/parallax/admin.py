from django.contrib import admin
from django.http import HttpResponseRedirect
from models import BlockContent, Page, ParallaxConfig, Contact, ParallaxConfigImage, ParallaxConfigAboutImage, \
    ParallaxConfigService, Team, Portfolio, Testimonial, PortfolioFeature, PortfolioImage


class ParallaxConfigImageInlineAdmin(admin.StackedInline):
    model = ParallaxConfigImage
    extra = 1

class ParallaxConfigAboutImageInlineAdmin(admin.StackedInline):
    model = ParallaxConfigAboutImage
    extra = 1

class ParallaxConfigServiceInlineAdmin(admin.StackedInline):
    model = ParallaxConfigService
    extra = 1

class ParallaxConfigAdmin(admin.ModelAdmin):
    inlines = [ParallaxConfigImageInlineAdmin, ParallaxConfigAboutImageInlineAdmin, ParallaxConfigServiceInlineAdmin]
    fieldsets = (
        (None, {
            'fields': (('parallax_id','colour',),('site_name','site_name_small',), ('alt_link', 'alt_link_title'), 'text_colour',),
            }),
        ("Social", {
            'fields': (('social_twitter','social_skype', 'social_facebook',),)
        }),
        ("Main Header", {
            'fields': ('title',('subtitle_style',"subtitle",),),
        }),
        ("Images", {
            'fields': ('logo', 'backdrop',)
        }),
        ("About", {
            'fields': (
                ('is_about', 'about_title',),
                ('about_subtitle_style', 'about_subtitle'), 'about_paragraph',
            )
        }),
        ("Service", {
            'fields': (
                ('is_service', 'services_title',),
                'services_text',
            )
        }),
        ("Team", {
            'fields': (
                ('is_team', 'team_title',),
                'team_text',
            )
        }),
       ("Testimonials", {
            'fields': (
                ('is_testimonials', 'is_testimonials_transparent',),
                'testimonials_text_colour', 'testimonials_backdrop'
            )
        }),
        ("Portfolio", {
            'fields': (
                ('is_portfolio', 'portfolio_title',),
                'portfolio_text',
            )
        }),
       ("Contact", {
            'fields': (
                ('is_contact', 'contact_title',), "contact_number",
                ('contact_location', "contact_email",),
                'contact_text',
            )
        }),

    )

    def changelist_view(self, request, extra_context=None):
       try:
           location = '/admin/parallax/parallaxconfig/%d' % ParallaxConfig.objects.get_or_create(id=1, defaults={})[0].id
           return HttpResponseRedirect(location)
       except:
           return super(ParallaxConfigAdmin, self).changelist_view(request, extra_context)

admin.site.register(ParallaxConfig, ParallaxConfigAdmin)


class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ['author', "display", 'order', "quote"]
    list_editable = ('display','order')
    list_filter = ('display',)
admin.site.register(Testimonial, TestimonialsAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ["name", 'title', "display", 'order']
    list_editable = ('display','order')
    list_filter = ('display',)
admin.site.register(Team, TeamAdmin)

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
    list_display = ('name', 'email',)
admin.site.register(Contact, ContactAdmin)

class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage

class PortfolioFeatureInline(admin.TabularInline):
    model = PortfolioFeature

class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': (('display','title','slug','order',),'button_value','image','description',),
            }),
        ("Block 1", {
            'fields': (('block1_title', 'block1_standard',), 'block1_image','block1_description',)
        }),
        ("Block 2", {
            'fields': (('block2_title', 'block2_standard',), 'block2_image','block2_description',)
        }),
        ("Block 3", {
            'fields': (('block3_title', 'block3_standard',), 'block3_image','block3_description',)
        }),
        ("Block 4", {
            'fields': (('block4_title', 'block4_standard',), 'block4_image','block4_description',)
        }),
    )

    inlines = [PortfolioImageInline, PortfolioFeatureInline]
    list_display = ('title', 'slug', 'display', 'order', )

admin.site.register(Portfolio, PortfolioAdmin)
