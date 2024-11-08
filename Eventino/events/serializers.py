from rest_framework import serializers
from users.models import User
from events.models import Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "organizer",
            "location",
            "date",
        ]
        read_only_fields = ["organizer_username"]
