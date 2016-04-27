from django.contrib import admin
from base.models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

admin.site.register(Contact, ContactAdmin)
