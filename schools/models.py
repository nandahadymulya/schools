from django.db import models

class School(models.Model):
  npsn = models.IntegerField()
  name = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  sector = models.CharField(max_length=255)
  district = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  province = models.CharField(max_length=255)
  zip_code = models.IntegerField()
  technology = models.IntegerField()
  resources = models.IntegerField()
  content = models.IntegerField()

  def __str__(self):
    return self.name
