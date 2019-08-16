
from django.apps import AppConfig

try:
    from local_settings import APPS
except ImportError:
    pass

default_app_config = 'leonardo_iconlink.Config'

if 'leonardo_iconlink' in APPS:
    LEONARDO_APPS = [
        'leonardo_iconlink'
    ]

    LEONARDO_OPTGROUP = 'Link widgets'

    LEONARDO_WIDGETS = [
        'leonardo_iconlink.widget.iconlink.models.PageIconLinkWidget'
    ]

    LEONARDO_CSS_FILES = [
        'iconlink/default.css'
    ]


class Config(AppConfig):
    name = 'leonardo IconLink'
    verbose_name = "IconLink"
