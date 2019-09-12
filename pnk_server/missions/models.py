from django.db import models
from django.conf import settings
from .choices import MISSION_CATEGORIES, MISSION_STATUSES


class Mission(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    discordURL = models.URLField(blank=True)
    videoURL = models.URLField(blank=True)
    category = models.CharField(max_length=3, choices=MISSION_CATEGORIES, default='FRE')
    location = models.CharField(max_length=150)
    feature_image = models.URLField(blank=True)
    mission_date = models.DateTimeField()
    mission_status = models.CharField(max_length=3, choices=MISSION_STATUSES, default='ACT')
    briefing = models.TextField(blank=True)
    debriefing = models.TextField(blank=True)
    commander = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='commander', on_delete=models.CASCADE)
    rsvp_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='rsvp_users', blank=True)
    attended_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='attended_users', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "PNK Mission #{} - {}".format(self.id, self.name)
