from django.db import models
from utils.models import BaseModel


class WordA(BaseModel):
    name_en = models.CharField(max_length=45, unique=True, null=False, db_comment='英文')
    phonetic_symbol = models.CharField(max_length=45, null=False, db_comment='音标')
    part_of_speech = models.CharField(max_length=20, db_comment='词性')
    name_zh = models.CharField(max_length=20, db_comment='中文')

    class Meta:
        db_table = 'tb_a'
        verbose_name = 'a开头的单词'
        verbose_name_plural = verbose_name
