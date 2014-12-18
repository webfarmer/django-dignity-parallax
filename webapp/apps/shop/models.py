from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db import models


class Category(models.Model):
    site = models.ForeignKey(Site, related_name="site_category")
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s - %s" % (self.site, self.title)

class Product(models.Model):
    site = models.ForeignKey(Site, related_name="site_product")

    title = models.CharField(max_length=255)

    category = models.ManyToManyField(Category)

    slug = models.SlugField()
    display = models.BooleanField(default=True)

    image = models.FileField(verbose_name="Image", upload_to='upload/product/', blank=True, null=True)

    content = models.TextField(blank=False, null=False, verbose_name="Content")

    meta_title = models.CharField("Title",max_length=255, null=True, blank=True)
    meta_description = models.CharField("Description",max_length=255, null=True, blank=True)
    meta_keywords = models.CharField("Keywords",max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Product"
        verbose_name_plural= "Products"

    def __unicode__(self):
        return self.title



class ProductType(models.Model):
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class ProductImage(models.Model):
    description = models.CharField(max_length=255)
    image = models.FileField(verbose_name="Image", upload_to='upload/product/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.description

    class Meta:
        ordering = ["description"]



class ProductSize(models.Model):
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class ProductCost(models.Model):
    product = models.ForeignKey(Product)

    product_type = models.ForeignKey(ProductType)
    size = models.ForeignKey(ProductSize)

    cost = models.FloatField(blank=True, null=False, default=0, verbose_name="Cost")
    qty = models.IntegerField(blank=True, null=False, default=0, verbose_name="QTY")
    notify_at_qty = models.IntegerField(blank=True, null=False, default=0, verbose_name="Notify at QTY")
    endless_qty = models.BooleanField(blank=True, null=False, default=True, verbose_name="Endless QTY")

    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.product.title


class Order(models.Model):
    site = models.ForeignKey(Site, related_name="site_order")
    user = models.ForeignKey(User)

    hq_email = models.EmailField(max_length=255)
    STATUS_CHOICES = (
        ('accept', 'Accept'),
        ('decline', 'Decline'),
    )

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="decline")

    comment = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order)

    product = models.ForeignKey(Product)

    qty = models.IntegerField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
