from django.db import models

from django_admin_geomap import GeoItem


# Create your models here.
class Place(models.Model, GeoItem):
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    rating = models.IntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(rating__range=(0, 25)),
                name='rating_constraint',
            ),
            models.CheckConstraint(
                check=models.Q(latitude__range=(-90, 90)),
                name='latitude_constraint',
            ),
            models.CheckConstraint(
                check=models.Q(longitude__range=(-180, 180)),
                name='longitude_constraint',
            )
        ]

    @property
    def geomap_latitude(self):
        return str(self.latitude)

    @property
    def geomap_longitude(self):
        return str(self.longitude)

    def __str__(self):
        return f'{self.name} {self.rating}/25'
