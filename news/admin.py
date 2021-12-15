# vim: set fileencoding=utf-8 :
from django.contrib import admin

#-------Importation----------#
from . import models
from django.utils.safestring import mark_safe



class News(admin.TabularInline):
    model =  models.New
    #-------------le nombre d element a ajouter----------------#
    extra = 0


class CompetitionAdmin(admin.ModelAdmin):

    inlines = [News]
    list_display = (
        'name',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'name',
    )
    
    search_fields = ('name',)
    date_hierarchy = 'date_add'
    actions = (
          'active',
          'desactive',
      )
    list_display_links = [
        'name',
        ]
    list_per_page = 100

    ordering = [
          'name',
      ]
    # readonly_fields = ['view_image']
    def active(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,"la selection a ete activer avec succes")
    active.short_description = "Activer les Competition selectionner"

    def desactive(self,request,queryset):
        queryset.update(status=False)
        self.message_user(request,"la selection a ete desactiver avec succes")
    desactive.short_description = "desactiver les Competition selectionner"

class NewAdmin(admin.ModelAdmin):

    list_display = (
        'image',
        'competition',
        'title',
        'date_pub',
        'author',
        'short_description',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = ('status', 'date_add', 'date_upd','competition',)
    search_fields = ('title',)
    date_hierarchy = 'date_add'
    actions = (
        'active',
        'desactive',
    )
    list_display_links = ['title',]
    list_per_page = 100
    ordering = ['title',]
    
    def view_image(self,obj):
        
        return mark_safe('<img src="{img_url}" width="100px", heigth="100px"/>'.format(img_url=obj.image))
    
    def active(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,"la selection a ete activer avec succes")
    active.short_description = "Activer les news selectionner"

    def desactive(self,request,queryset):
        queryset.update(status=False)
        self.message_user(request,"la selection a ete desactiver avec succes")
    desactive.short_description = "desactiver les news selectionner"




def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Competition, CompetitionAdmin)
_register(models.New, NewAdmin)
