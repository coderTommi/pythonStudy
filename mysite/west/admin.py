from django.contrib import admin
from west.models import Character,Contact,Tag
# Register your models here.

class TagInline(admin.TabularInline):
    model=Tag

class ContactAdmin(admin.ModelAdmin):
    #fields=('name','email')
    inlines=[TagInline]
    fieldsets=(
        ['Main' , {'fields':('name','email')}],
        ['Advance',{'classes':('colllapse',),'fields':('age',),}]
    )
    list_display=('name','age','email')
    search_fields=('name','email')

admin.site.register(Contact, ContactAdmin)
admin.site.register([Character,Tag])
