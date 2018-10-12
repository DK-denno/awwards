from rest_framework import serializers
from .models import Posts,Profile

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id','user','name','link','image1','image2','image3','video','postedon']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','user','dp','bio','phone_number']