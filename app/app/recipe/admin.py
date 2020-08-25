from django.contrib import admin
from recipe import models
# Register your models here.
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')


admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Ingredient)
admin.site.register(models.Recipe)