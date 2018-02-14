from django.contrib import admin

from .models import Type, Topic, Entry

admin.site.register(Type)
admin.site.register(Topic)
admin.site.register(Entry)
