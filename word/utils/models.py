from django.db import models


class BaseModel(models.Model):
    """
    为模型类补充字段
    """
    create_at = models.DateTimeField(auto_now_add=True, db_comment='创建时间')
    update_at = models.DateTimeField(auto_now=True, db_comment='更新时间')

    class Meta:
        # 说明是抽象模型类, 用于继承使用，数据库迁移时不会创建BaseModel的表
        abstract = True
