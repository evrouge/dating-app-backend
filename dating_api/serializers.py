from rest_framework import serializers
from .models import Dating

### ALLOWS YOU TO CREATE AND CHECK PASSWORDS
from django.contrib.auth.hashers import make_password, check_password

class DatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dating
        fields = ('id', 'email', 'password', 'name', 'age', 'ethnicity', 'location', 'hobbies', 'occupation', 'image' )

    ### THIS HASHES A NEW USERS PASSWORD WHEN THEY CREATE AN ACCOUNT
    def create(self, validated_data):
        user = Dating.objects.create(
        email=validated_data['email'],
        password = make_password(validated_data['password']),
        name=validated_data['name'],
        age=validated_data['age'],ethnicity=validated_data['ethnicity'],location=validated_data['location'],hobbies=validated_data['hobbies'],occupation=validated_data['occupation'],image=validated_data['image']
        )
        user.save()
        return user

    ### THIS MAKES SURE THEIR UPDATED PASSWORDS ARE ALSO HASHED
    def update(self,instance, validated_data):
        user = Dating.objects.get(
        email=validated_data['email'])
        user.name=validated_data['name']
        user.age=validated_data['age']
        user.email=validated_data['email']
        user.ethnicity=validated_data['ethnicity']
        user.hobbies=validated_data['hobbies']
        user.image=validated_data['image']
        user.location=validated_data['location']
        user.occupation=validated_data['occupation']
        user.password = make_password(validated_data["password"])
        user.save()
        return user
