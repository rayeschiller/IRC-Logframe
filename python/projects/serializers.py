from rest_framework import serializers

from .models import Project, Objective


class ObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objective
        fields = ('title',)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('created_at', 'updated_at', 'id', 'title', 'goal', 'created_by', 'modified_by', 'donor', 'objectives') 
