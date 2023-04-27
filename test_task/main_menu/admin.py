from django.contrib import admin
from main_menu.models import Child, Parent


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'url')


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'url', 'parent')
