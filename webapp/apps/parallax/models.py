from django.db import models

class BlockContent(models.Model):
    slug = models.SlugField(max_length=150)
    display = models.BooleanField(default=True, blank=True)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Block Content"
        verbose_name_plural = "Block Content"


class Page(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    slug =  models.SlugField(max_length=150,blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    display = models.BooleanField(default=True, blank=True)

    meta_title = models.CharField("Title",max_length=255, null=True, blank=True)
    meta_description = models.CharField("Description",max_length=255, null=True, blank=True)
    meta_keywords = models.CharField("Keywords",max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"


class HomeConfig(models.Model):
    meta_title = models.CharField("Title",max_length=255, null=True, blank=True)
    meta_description = models.CharField("Description",max_length=255, null=True, blank=True)
    meta_keywords = models.CharField("Keywords",max_length=255, null=True, blank=True)

    landing_image = models.FileField(verbose_name="Image", upload_to='upload/image/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"


class HomeConfigHeaderImage(models.Model):
    config = models.ForeignKey(HomeConfig)
    image = models.FileField(verbose_name="Image", upload_to='upload/image/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
