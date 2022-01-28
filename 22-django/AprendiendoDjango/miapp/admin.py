from django.contrib import admin
from .models import *
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

#Configurar el titulo del panel
title = "Máster en Python - Víctor Robles 5"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = 'Panel de Gestión'