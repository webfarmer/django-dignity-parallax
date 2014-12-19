from django.db import models



class ParallaxConfig(models.Model):
    PARALLAX_CHOICES =(
        ("01",'index01.html'),
        ("02",'index02.html'),
        ("03",'index03.html'),
        ("04",'index04.html'),
        ("05",'index05.html'),
        ("06",'index06.html'),
        ("07",'index07.html'),
        ("08",'index08.html'),
        ("09",'index09.html'),
        ("10",'index10.html'),
    )
    parallax_id = models.CharField(max_length=255, choices=PARALLAX_CHOICES)

    title = models.CharField(max_length=255, blank=True, null=True)
    site_name = models.CharField(max_length=255, blank=True, null=True)

    logo = models.FileField(verbose_name="Main Image", upload_to='upload/parallax/', blank=True, null=True)


    contact_text = models.TextField(blank=True, null=True)
    contact_company_name = models.CharField(max_length=255, blank=True, null=True)
    contact_company_email = models.CharField(max_length=255, blank=True, null=True)

    social_twitter = models.CharField(max_length=255, blank=True, null=True)
    social_skype = models.CharField(max_length=255, blank=True, null=True)
    social_facebook = models.CharField(max_length=255, blank=True, null=True)


    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = "Configurations"
        verbose_name_plural = "Configurations"

class ParallaxConfigImage(models.Model):

    title = models.CharField(max_length=255, blank=False, null=True)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = "Configurations"
        verbose_name_plural = "Configurations"


class Team(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=False, null=True)
    description = models.CharField(max_length=255, blank=False, null=True)

    image = models.FileField(verbose_name="Image", upload_to='upload/team/', blank=True, null=True)

    display = models.BooleanField(default=True, blank=True)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Team"


class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=False, null=True)
    display = models.BooleanField(default=True, blank=True)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Team"

class Contact(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=30)
    message = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-created_at']


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
