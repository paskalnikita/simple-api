from django.contrib import admin
from .models import Message, ViewsCounter

admin.site.register(Message)
admin.site.register(ViewsCounter)
