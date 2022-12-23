from rest_framework import serializers
from .models import Dating

class DatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dating
        fields = ('id', 'name', 'age', 'ethnicity', 'location', 'hobbies', 'occupation', 'image', )
