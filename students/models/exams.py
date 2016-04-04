
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Exam(models.Model):
    """Exam Model"""
    class Meta(object):
        verbose_name = _(u"Exam")
        verbose_name_plural = _(u"Exams")
        ordering = ['date']

    subject = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_(u'Subject'))

    date = models.DateTimeField(
        blank=False,
        verbose_name=_(u'Date'))

    teacher=models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_(u'Teacher'))

    group = models.OneToOneField('Group',
        verbose_name=_(u"Group"),
        blank=False)

    def __unicode__(self):
        return u"%s %s %s %s" % (self.subject, self.teacher, self.date, self.group)
