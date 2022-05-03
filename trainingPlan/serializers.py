from rest_framework import serializers
from .models.plan import Plan, Category

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('id', 'title', 'desc', 'price', 'published', 'pdf', 'image', 'coach', 'status', 'category')