from django.db import models
from django.conf import settings

SCHOOLS = "SCHOOLS"

class School(models.Model):
  npsn = models.IntegerField()
  name = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  sector = models.CharField(max_length=255)
  district = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  province = models.CharField(max_length=255)
  zip_code = models.IntegerField()
  people = models.IntegerField()
  technology = models.IntegerField()
  inovation = models.IntegerField()
  self_development = models.IntegerField()

  def __str__(self):
    return self.name
