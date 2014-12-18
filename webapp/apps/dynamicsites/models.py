from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db.models import FileField, CharField, ForeignKey
from dynamicsites.fields import SubdomainListField, FolderNameField

"""
Monkey-patch the Site object to include a list of subdomains
Future ideas include:
* Site-enabled checkbox
* Site-groups
* Account subdomains (ala basecamp)
"""

FolderNameField(blank=True).contribute_to_class(Site,'folder_name')
SubdomainListField(blank=True).contribute_to_class(Site,'subdomains')
ForeignKey(User, null=True, blank=True).contribute_to_class(Site,'Officer')
CharField("Company Title", max_length=255, null=True, blank=True).contribute_to_class(Site,'company')
FileField("Logo",max_length=255, null=True, blank=True, upload_to='logo/').contribute_to_class(Site,'logo')
CharField("Google Analytics Code", max_length=255, null=True, blank=True).contribute_to_class(Site,'ga_code')
CharField("Meta Description", max_length=255, null=True, blank=True).contribute_to_class(Site,'meta_description')
CharField("Prefix", max_length=255, null=True, blank=True).contribute_to_class(Site,'prefix')


@property
def has_subdomains(self):
    return len(self.subdomains)

@property
def default_subdomain(self):
    """
    Return the first subdomain in self.subdomains or '' if no subdomains defined
    """
    if len(self.subdomains):
        if self.subdomains[0]=="''":
            return ''
        return self.subdomains[0]
    return ''

Site.has_subdomains = has_subdomains
Site.default_subdomain = default_subdomain

