from rest_framework import serializers
from ..models import School

class SchoolSerializer(serializers.ModelSerializer):
  class Meta:
    model = School
    fields = ('id', 'npsn', 'name', 'address', 'sector', 'district', 'city', 'province', 'zip_code', 'technology', 'resources', 'content')
    