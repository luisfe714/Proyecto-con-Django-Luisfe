from django.contrib import admin
from .models import Page

#Configuracion extra
class PageAdmin(admin.ModelAdmin):
    readonly_field = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('visible',) #NO se puede poner solo el valor porque esta esperando una tupla
    list_display = ('title','visible','created_at')
    ordering = ('-created_at',)

# Register your models here.
admin.site.register(Page, PageAdmin)

#Configuracion del panel
title = "Proyecto con Django"
subtitle = "Panel de Gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle