from django.contrib import admin
from blackjack.models import Object


class ObjectAdmin(admin.ModelAdmin):
    list_display = ['number', 'name', 'code', 'inv', 'price', 'count', 'summ', 'note']


admin.site.register(Object, ObjectAdmin)