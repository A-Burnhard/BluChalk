from rest_framework import serializers
from .models import Forum, Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class ForumSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Forum
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'messages']

