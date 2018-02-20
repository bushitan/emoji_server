# -*- coding: utf-8 -*-
from django.contrib import admin
from lite.models import *

# class UserAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(User,UserAdmin)



class UserAdmin(admin.ModelAdmin):
   list_display = ('id','is_vip','uuid','vip_deadline',)
   list_filter = ('is_vip',) #右边过滤器
   search_fields = ('uuid',)
admin.site.register(User,UserAdmin)

class OrderAdmin(admin.ModelAdmin):
   list_display = ('id','user_id','is_pay','pay_price','pay_time','create_time',)
   list_filter = ('is_pay','pay_time','create_time',) #右边过滤器
admin.site.register(Order,OrderAdmin)

class ImageAdmin(admin.ModelAdmin):
   fields = ['cover_pre','url','local_path',]
   list_display = ('id','cover_pre','url',)
   list_editable = ('url',)
   def cover_pre(self, obj):
      if obj.url != "":
         html = u'<img src="%s?imageMogr2/thumbnail/72x72" style="width:72px;height:48px" />' %(obj.url)
      else:
         html = u"未添加封面"
      return html
   cover_pre.short_description = u'封面图片预览'
   cover_pre.allow_tags = True  # 允許執行 image_tag 中回傳的 html 語法，若為 False(預設)則會被視為純文字
   readonly_fields = ['cover_pre',]
admin.site.register(Image,ImageAdmin)