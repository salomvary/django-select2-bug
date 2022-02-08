from django.db import models

class OtherThing(models.Model):
    pass


class Thing(models.Model):
    other_things = models.ForeignKey(OtherThing, on_delete=models.CASCADE)
