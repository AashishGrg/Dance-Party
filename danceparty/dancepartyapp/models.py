# Create your models here.
from django.contrib.auth.models import User
from django.db import models

"""
Table 1​ should include columns- 
Location of dance party (link to dance party page), 
party start datetime, 
party end time, 
the theme of party, 
leave party link. 
When the logged in user creates a dance party they should automatically be “joined” to that party and 
it should be listed here.
"""


class DanceParty(models.Model):
    PARTY_THEMES = (
        ('BIRTHDAY_PARTY', 'BIRTHDAY_PARTY'),
        ('TEA_PARTY', 'TEA_PARTY'),
        ('WEDDING_PARTY', 'WEDDING_PARTY'),
        ('OTHER', 'OTHER')
    )

    page_link = models.CharField(max_length=100)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    theme = models.CharField(max_length=50, choices=PARTY_THEMES, default='OTHER')
    participants = models.ManyToManyField(User)

    def __str__(self):
        return 'page link - {}, theme - {}'.format(self.page_link, self.theme)
