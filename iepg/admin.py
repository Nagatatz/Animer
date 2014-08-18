# -*- coding: utf-8 -*-

#from iepg.models import Program, Title, Waves, Station, Comments
from iepg.models import Program, Title, Comments, Favorites
from django.contrib import admin

class ProgramInline(admin.StackedInline):
    model = Program
    extra = 1
#
class TitleAdmin(admin.ModelAdmin):
    inlines = [ProgramInline]
#

class FavoritesInline(admin.StackedInline):
    model = Favorites
    extra = 1

class UserAdmin(admin.ModelAdmin):
    inlines = [FavoritesInline]

#admin.site.register(Title,TitleAdmin)

admin.site.register(Program)
admin.site.register(Title)
#admin.site.register(Waves)
#admin.site.register(Station)
admin.site.register(Comments)

#admin.site.register(Program)

admin.site.register(Favorites)
