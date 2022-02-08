from django.contrib import admin

from .models import Thing, OtherThing

class OtherThingAdmin(admin.ModelAdmin):
    search_fields = ("pk",)

class ThingAdmin(admin.ModelAdmin):
    autocomplete_fields = ("other_things",)


admin.site.register(OtherThing, OtherThingAdmin)
admin.site.register(Thing, ThingAdmin)
