from django.contrib import admin

# Register your models here.
from .models import Event, Guest, Type, JuncGuestGroup, JuncEventType, EventOwner, EventAatendee

admin.site.register(Event)
admin.site.register(Guest)
admin.site.register(Type)
admin.site.register(JuncGuestGroup)
admin.site.register(JuncEventType)
admin.site.register(EventOwner)
admin.site.register(EventAatendee)