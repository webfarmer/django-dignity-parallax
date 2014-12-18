from django.db import models


class EmailContent(models.Model):
    name =  models.CharField(max_length=100, blank=False, null=False)
    slug =  models.SlugField(max_length=150,blank=False, null=False)
    subject = models.CharField(max_length=150)
    body_html = models.TextField(blank=False, null=False)
    body_text = models.TextField(blank=False, null=False)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Email Template"
        verbose_name_plural = "Email Templates"

