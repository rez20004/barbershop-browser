from django.db.models import Model, CharField
from django.contrib.gis.db.models import PointField

class Location(Model):
    name = CharField(max_length=140)
    point = PointField()