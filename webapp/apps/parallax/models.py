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

    COLOUR_CHOICES =(
        ("red",'Red'),
        ("yellow",'Yellow'),
        ("green",'Green'),
        ("blue",'Blue'),
    )
    colour = models.CharField(max_length=255, choices=COLOUR_CHOICES, blank=True, null=True)

    site_name = models.CharField(max_length=255, blank=True, null=True)
    site_name_small = models.CharField(max_length=255, blank=True, null=True)
    TEXT_COLOUR_CHOICES =(
        ("black",'Black'),
        ("white",'White'),
    )
    text_colour = models.CharField(max_length=255, choices=TEXT_COLOUR_CHOICES, blank=True, null=True)

    alt_link = models.URLField(blank=True, null=True)
    alt_link_title = models.CharField(max_length=255, blank=True, null=True)

    backdrop = models.FileField(verbose_name="Backdrop", upload_to='upload/parallax/', blank=True, null=True)

    logo = models.FileField(verbose_name="Logo", upload_to='upload/parallax/', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    subtitle_style = models.CharField(max_length=255, blank=True, null=True)

    about_logo = models.FileField(verbose_name="About Logo", upload_to='upload/parallax/', blank=True, null=True)
    about_title = models.CharField(max_length=255, blank=True, null=True)
    about_subtitle = models.CharField(max_length=255, blank=True, null=True)
    about_subtitle_style = models.CharField(max_length=255, blank=True, null=True)
    about_paragraph = models.TextField(blank=True, null=True)
    about_backdrop = models.FileField(verbose_name="About Backdrop", upload_to='upload/parallax/', blank=True, null=True)

    testimonials_backdrop = models.FileField(verbose_name="Testimonial Backdrop", upload_to='upload/parallax/', blank=True, null=True)
    is_testimonials_transparent = models.BooleanField(default=True, blank=True)
    testimonials_text_colour = models.CharField(max_length=255, choices=TEXT_COLOUR_CHOICES, blank=True, null=True)

    services_title = models.CharField(max_length=255, blank=True, null=True)
    services_text = models.TextField(blank=True, null=True)

    portfolio_title = models.CharField(max_length=255, blank=True, null=True)
    portfolio_text = models.TextField(blank=True, null=True)

    team_title = models.CharField(max_length=255, blank=True, null=True)
    team_text = models.TextField(blank=True, null=True)

    contact_title = models.CharField(max_length=255, blank=True, null=True)
    contact_text = models.TextField(blank=True, null=True)
    contact_location = models.CharField(max_length=255, blank=True, null=True)
    contact_number = models.CharField(max_length=255, blank=True, null=True)
    contact_email = models.CharField(max_length=255, blank=True, null=True)

    social_twitter = models.CharField(max_length=255, blank=True, null=True)
    social_skype = models.CharField(max_length=255, blank=True, null=True)
    social_facebook = models.CharField(max_length=255, blank=True, null=True)

    is_about = models.BooleanField(default=True, blank=True)
    is_service = models.BooleanField(default=True, blank=True)
    is_team = models.BooleanField(default=True, blank=True)
    is_testimonials = models.BooleanField(default=True, blank=True)
    is_portfolio = models.BooleanField(default=True, blank=True)
    is_contact = models.BooleanField(default=True, blank=True)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    def get_parallaxconfigservice(self):
        return self.parallaxconfigservice_set.filter(display=True)

    def get_parallaxconfigimage(self):
        return self.parallaxconfigimage_set.filter(display=True)

    def get_parallaxconfigaboutimage(self):
        return self.parallaxconfigaboutimage_set.filter(display=True)

    class Meta:
        verbose_name = "Configurations"
        verbose_name_plural = "Configurations"

class ParallaxConfigImage(models.Model):
    parallax = models.ForeignKey(ParallaxConfig)

    title = models.CharField(max_length=255, blank=False, null=True)
    image = models.FileField(verbose_name="Main Image", upload_to='upload/parallax/bg/', blank=True, null=True)
    display = models.BooleanField(default=True, blank=True)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Bg Image"
        verbose_name_plural = "Bg Image"

class ParallaxConfigAboutImage(models.Model):
    parallax = models.ForeignKey(ParallaxConfig)

    title = models.CharField(max_length=255, blank=False, null=True)
    image = models.FileField(verbose_name="Main Image", upload_to='upload/parallax/about/', blank=True, null=True)
    display = models.BooleanField(default=True, blank=True)
    order = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["order"]
        verbose_name = "About Images"
        verbose_name_plural = "About Images"

class ParallaxConfigService(models.Model):
    parallax = models.ForeignKey(ParallaxConfig)

    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)

    order = models.IntegerField(default=0)
    display = models.BooleanField(default=True, blank=True)
    emblem = models.FileField(verbose_name="Main Image", upload_to='upload/parallax/about/', blank=True, null=True)

    copy = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.title


    class Meta:
        ordering = ["order"]
        verbose_name = "Service"
        verbose_name_plural = "Service"


class Team(models.Model):
    name = models.CharField(max_length=255)
    display = models.BooleanField(default=True, blank=True)

    order = models.IntegerField(default=0)

    title = models.CharField(max_length=255, blank=False, null=True)
    description = models.TextField(blank=True, null=True)

    image = models.FileField(verbose_name="Image", upload_to='upload/parallax/team/', blank=True, null=True)

    social_twitter = models.CharField(max_length=255, blank=True, null=True)
    social_skype = models.CharField(max_length=255, blank=True, null=True)
    social_facebook = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["order"]
        verbose_name = "Team"
        verbose_name_plural = "Team"

class Testimonial(models.Model):
    display = models.BooleanField(default=True, blank=True)
    author = models.CharField(max_length=255)
    emblem = models.FileField(verbose_name="Image", upload_to='upload/parallax/portfolio/', blank=True, null=True)
    quote = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.quote

    class Meta:
        ordering = ["order"]
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonial"


class Portfolio(models.Model):

    title = models.CharField(max_length=255)

    slug = models.SlugField()

    display = models.BooleanField(default=True, blank=True)

    order = models.IntegerField(default=0)

    image = models.FileField(verbose_name="Image", upload_to='upload/parallax/portfolio/', blank=True, null=True)

    button_value = models.CharField(max_length=255, blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    block1_title = models.CharField(verbose_name="Title", max_length=255, blank=True, null=True)
    block1_standard = models.IntegerField(verbose_name="Standard Icon", blank=True, null=True, default=1)
    block1_description = models.TextField(verbose_name="Description",blank=True, null=True)
    block1_image = models.FileField(verbose_name="Image", upload_to='upload/parallax/portfolio/', blank=True, null=True)

    block2_title = models.CharField(verbose_name="Title",max_length=255, blank=True, null=True)
    block2_standard = models.IntegerField(verbose_name="Standard Icon",blank=True, null=True, default=2)
    block2_description = models.TextField(verbose_name="Description",blank=True, null=True)
    block2_image = models.FileField(verbose_name="Image", upload_to='upload/parallax/portfolio/', blank=True, null=True)

    block3_title = models.CharField(verbose_name="Title",max_length=255, blank=True, null=True)
    block3_standard = models.IntegerField(verbose_name="Standard Icon",blank=True, null=True, default=3)
    block3_description = models.TextField(verbose_name="Description",blank=True, null=True)
    block3_image = models.FileField(verbose_name="Image", upload_to='upload/parallax/portfolio/', blank=True, null=True)

    block4_title = models.CharField(verbose_name="Title",max_length=255, blank=True, null=True)
    block4_standard = models.IntegerField(verbose_name="Standard Icon",blank=True, null=True, default=4)
    block4_description = models.TextField(verbose_name="Description", blank=True, null=True)
    block4_image = models.FileField(verbose_name="Image", upload_to='upload/parallax/portfolio/', blank=True, null=True)


    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.title

    def get_features(self):
        return self.portfoliofeature_set.filter(display=True)

    def get_images(self):
        return self.portfolioimage_set.filter(display=True)


    class Meta:
        ordering = ["order"]
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolio"

class PortfolioFeature(models.Model):
    portfolio = models.ForeignKey(Portfolio)

    title = models.CharField(max_length=255)

    display = models.BooleanField(default=True, blank=True)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return ""


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio)

    image = models.FileField(verbose_name="Image", upload_to='upload/parallax/portfolio/', blank=True, null=True)
    display = models.BooleanField(default=True, blank=True)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.portfolio.title


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
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
