from django.contrib import admin
from models import Product, ProductCost, ProductSize, ProductType, Order


class ProductCostInline(admin.TabularInline):
    model = ProductCost

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductCostInline,]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']
    list_display = ('title', 'slug', 'display')
    list_filter = ('display',)
    list_editable = ('display','slug',)
    fieldsets = (
        (None, {
            'fields': ('site',('display','title','slug',),"category",'image',),
            }),
            ("Meta Details", {
                'classes': ('collapse',),
                'fields': (('meta_title', 'meta_description', 'meta_keywords',),)
            }),
    )
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)



class ProductNoAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}
admin.site.register(ProductType, ProductNoAdmin)
admin.site.register(ProductSize, ProductNoAdmin)
