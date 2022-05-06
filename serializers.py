from rest_framework import serializers
from .models import (
    District,
    Upazila,
    Union,
)


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        fields = (
            'id',
            'name'
        )
