"""
Definition of models.
"""

from django.db import models

class Contact(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    email_address = models.EmailField()
    contact_date = models.DateTimeField(auto_now_add=True)
    how_would_you_use = models.TextField()

    def __str__(self):
        return "%s (%s)" % (self.name, self.email_address,)


