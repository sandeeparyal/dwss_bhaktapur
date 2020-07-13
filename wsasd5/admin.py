from django.contrib import admin

from .models import Employee, Position, News, Document
# Register your models here.

admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(News)
admin.site.register(Document)


