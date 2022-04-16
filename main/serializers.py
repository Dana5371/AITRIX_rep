from rest_framework import serializers
from django.utils import timezone
from main.models import *
from datetime import timedelta


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'



class AnnouncementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Announcement
        exclude = ('author',)

    def create(self, validated_data):
        request = self.context.get('request')
        user_id = request.user.id
        validated_data['author_id'] = user_id
        ad = Announcement.objects.create(**validated_data)
        return ad
    
    def get_queryset(self):
        queryset = super().get_queryset()
        days_count = int(self.request.query_params.get('day', 0))
        if days_count > 0:
            start_date = timezone.now() - timedelta(days=days_count)
            queryset = queryset.filter(created__gte=start_date)
        return queryset



    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = instance.author.email
        return representation
