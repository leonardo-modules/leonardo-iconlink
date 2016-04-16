
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


default_app_config = 'leonardo_iconlink.Config'


class Default(object):

    optgroup = 'Web'

    apps = [
        'leonardo_iconlink'
    ]

    widgets = [
        'leonardo_iconlink.models.PageIconLinkWidget'
    ]


class Config(AppConfig, Default):
    name = 'leonardo_iconlink'
    verbose_name = _("IconLink")

default = Default()
