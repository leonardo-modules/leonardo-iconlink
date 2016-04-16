# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from leonardo.module.web.models import Widget
from leonardo.module.web.models import Page

from .const import ICON_CHOICES, SIZE_CHOICES


class PageIconLinkWidget(Widget):

    """
    Font Awesome (the fist library) Page Icon Link Widget

    * http://fortawesome.github.io/Font-Awesome/icons/
    """

    icon = models.CharField(
        max_length=255, verbose_name=_("Icon"), choices=ICON_CHOICES)

    size = models.CharField(
        max_length=255, verbose_name=_("Size"), choices=SIZE_CHOICES, default='normal')

    spin = models.BooleanField(default=False, verbose_name=_("Spin"))

    border = models.BooleanField(default=False, verbose_name=_("Border"))

    animated = models.BooleanField(default=False, verbose_name=_("Animated"))

    onpage = models.BooleanField(defauld=True, verbose_name=_("Link to the section on this page"))

    circle = models.BooleanField(defauld=False, verbose_name=_("Circle appearance"))

    link = models.ForeignKey(Page, blank=True, null=True,
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