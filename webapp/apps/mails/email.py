from django.template.defaultfilters import slugify
import os, errno, time
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from models import EmailContent
from django.template import Context, Template
from django.utils.html import strip_tags

class myMailer():
    slug = "contact"
    lang = 'en'
    from_email = settings.EMAIL_SYSTEM_SENDER
    subject = None
    to = None
    context =  None
    user = None

    def __init__(self, *args, **kwargs):
        if kwargs.get('slug'): self.slug = kwargs.get('slug')
        if kwargs.get('lang'): self.lang = kwargs.get('lang')
        if kwargs.get('to'): self.to = kwargs.get('to')
        if kwargs.get('from_email'): self.from_email = kwargs.get('from_email')
        if kwargs.get('subject'): self.subject = kwargs.get('subject')
        self.context = Context(kwargs)

    def get_object(self):
        return EmailContent.objects.get(slug=self.slug)

    def mkdir_p(self, path):
        try:
            os.makedirs(path)
        except OSError as exc: # Python >2.5
            if exc.errno == errno.EEXIST:
                pass
            else: raise

    def send(self):
        object = self.get_object()

        from_email, to = self.from_email, self.to
        subject, html_content = object.subject, object.content

        if not self.subject:
            self.context['subject'] = strip_tags(Template(subject).render(self.context))
        else:
            self.context['subject'] = self.subject

        html_content = '{% extends "mails/base.html" %}{% block content %}' + html_content + '{% endblock %}'

        if to:
            if not type(to) is list:
                to = [to]
            msg = EmailMultiAlternatives(self.context['subject'], Template(html_content).render(self.context), from_email, to)
            msg.attach_alternative(Template(html_content).render(self.context), "text/html")

            if settings.MAIL_WRITE_TO_HDD:
                TEST_EMAIL_DIR = os.path.join(settings.PROJECT_DIR, "tmp")
                self.mkdir_p(TEST_EMAIL_DIR)
                filename = os.path.join(TEST_EMAIL_DIR, "%s_%s__%s.eml" % (time.time().__int__().__str__(), self.slug, slugify(self.subject)) )
                if not os.path.isdir(TEST_EMAIL_DIR): os.mkdir(TEST_EMAIL_DIR)
                f = open(filename, 'w')
                f.write(msg.message().as_string())
                f.close()
            else:
                msg.send()
