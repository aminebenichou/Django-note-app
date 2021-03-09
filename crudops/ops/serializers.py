from rest_framework import serializers
from .models import Notes


class NotesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notes
        fields = ('title', 'text', 'userid')