from django import forms
from django.contrib.sites.models import Site

from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from mails.email import myMailer

from models import Contact
from django.conf import settings


class ContactForm(forms.Form):
    name = forms.CharField(label=_("Name"), widget=forms.TextInput(attrs={"placeholder":_("Name")}))
    email = forms.EmailField(label=_("Email"), widget=forms.TextInput(attrs={"placeholder":_("Email")}))
    message = forms.CharField(label=_("Message"), widget=forms.Textarea(attrs={'style':'height:60px', "placeholder":_("Message")}))

    def save(self, request, profile_callback=None):
        contact = Contact.objects.create(
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            message=self.cleaned_data['message'],
        ); contact.save()

        site_url = ('%s%s') % ('http://', request.get_host())
        link = '<a href="%s%s">%s</a>' % (site_url,('/admin/pages/contact/%s' % contact.id),"%s" % self.cleaned_data['name'])

        mail = myMailer(slug = "contact",
            to=settings.WEBCONTACT_RECIPIENTS,
            subject = "%s has made contact" % self.cleaned_data['name'],
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            message=self.cleaned_data['message'],
            link=mark_safe(link),
            site_url=mark_safe(site_url)
        ); mail.send()