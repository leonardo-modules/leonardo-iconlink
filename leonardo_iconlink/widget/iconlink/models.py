# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from leonardo.module.web.models import IconWidget
from leonardo.module.web.models import Page

class PageIconLinkWidget(IconWidget):

    animated = models.BooleanField(default=False, verbose_name=_("Animated"))

    onpage = models.BooleanField(default=True, verbose_name=_("Link to the section on this page"))

    circle = models.BooleanField(default=False, verbose_name=_("Circle appearance"))

    link = models.ForeignKey(Page,
                             verbose_name=_("Link"),
                             related_name="context_link", help_text=_(
                                 'Scroll on the page you want.'))

    def get_link(self, request=None):

        if self.link:
            link = self.link
        else:
            if not request:
                raise Exception(
                    'call populate_items with request before access to data')
            link = request.leonardo_page
        return link

    class Meta:
        abstract = True
        verbose_name = _('Icon Link')
        verbose_name_plural = _('Icon Links')