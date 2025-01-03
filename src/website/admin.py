from django.contrib import admin
from website.models import Record

# Register your models here.
@admin.register(Record)
class Recordadmin(admin.ModelAdmin):
    pass