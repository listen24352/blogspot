import os
from django.apps import AppConfig

default_app_config = 'apps.vocabulary.VocabularyConfig'


def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


class VocabularyConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = '词汇大纲'
