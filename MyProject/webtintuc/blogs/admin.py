from django.contrib import admin
from .models import theloai, baiviet

# Register your models here.


class sapxeptheloai(admin.ModelAdmin):
    list_display = ['tentheloai']
admin.site.register(theloai,sapxeptheloai)

class chinhbaiviet(admin.ModelAdmin):
    list_display = ['tenbaiviet', 'ngay']
    list_filter = ['ngay']
    search_fields = ['tenbaiviet']
admin.site.register(baiviet, chinhbaiviet)