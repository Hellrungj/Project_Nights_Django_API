from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.

class Guest(models.Model):
    username = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class JuncGuestGroup(models.Model):
    guest_id = models.ForeignKey(Guest, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [["guest_id", "group_id"]]

    def __str__(self):
        return "%s %s" % (self.guest_id, self.group_id)

class Event(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    date_time = models.DateTimeField(null=False)
    location = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class JuncEventType(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [["event_id", "type_id"]]

    def __str__(self):
        return "%s %s" % (self.event_id, self.type_id)

class EventAatendee(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [["event_id", "user_id"]]

    def __str__(self):
        return "%s %s" % (self.event_id, self.user_id)

class EventOwner(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [["event_id", "user_id"]]

    def __str__(self):
        return "%s %s" % (self.event_id, self.user_id)