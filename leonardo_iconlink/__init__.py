
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

try:
    from local_settings import APPS
except ImportError:
    pass

    default_app_config = 'leonardo_iconlink.Config'

class Default(object):

    if 'leonardo_iconlink' in APPS:
        optgroup = 'Link widgets'

        apps = [
            'leonardo_iconlink'
        ]

        css_files = [
            'iconlink/default.css'
        ]

        widgets = [
            'leonardo_iconlink.widget.iconlink.models.PageIconLinkWidget'
        ]


class Config(AppConfig, Default):
    name = 'leonardo_iconlink'
    verbose_name = _("IconLink")

default = Default()
