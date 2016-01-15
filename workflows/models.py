from django.db import models


class Step(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    # inputs = models.ManyToManyField("self", blank=True, null=True)