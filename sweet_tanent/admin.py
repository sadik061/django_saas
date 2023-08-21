from django.contrib import admin

from sweet_tanent.models import Sweet
# Register your models here.


@admin.register(Sweet)
class SweetAdmin(admin.ModelAdmin):
    list_display = ('name','sweet_type',)
