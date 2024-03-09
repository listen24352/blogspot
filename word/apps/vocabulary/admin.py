from django.contrib import admin
from apps.vocabulary.models import WordA

# 修改title和header
admin.site.site_title = 'blogs'
admin.site.site_header = '自考英语二（单词）'


@admin.register(WordA)
class WordAAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_en', 'phonetic_symbol', 'part_of_speech', 'name_zh', 'update_at']  # 设置显示的字段
    # fields
    # exclude
    # exclude = ['id', 'name_en', 'phonetic_symbol', 'part_of_speech', 'name_zh']  # 不允许修改
    ordering = ['id']  # ['id']为升序，['-id']为降序
    # 设置可搜索的字段
    search_fields = ['name_en', 'name_zn']

    # 设置动作栏的位置
    actions_on_top = False
    actions_on_bottom = True
    # 日期选择器
    date_hierarchy = 'update_at'
    # 设置过滤器
    list_filter = ['part_of_speech']
