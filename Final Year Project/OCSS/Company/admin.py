from django.contrib import admin

# Register your models here.
from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('cid', 'c_name', 'address', 'city', 'state', 'pin_code', 'email', 'cp_name', 'c_website', 'contact_no')
    list_display_links = ('cid','c_name')
    search_fields = ('c_name', 'cp_name')
    list_per_page = 25

admin.site.register(Company, CompanyAdmin)


