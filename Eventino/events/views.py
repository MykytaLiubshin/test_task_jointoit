from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import jwt
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet, DateFilter
from users.permissions import IsAuthedUser
from events.serializers import EventSerializer
from events.models import Event


class DateFilter(FilterSet):
    class Meta:
        model = Event
        fields = {
            "date": ["lte", "gte"],
            "title": ["iexact", "icontains"],
        }

class EventsListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthedUser]
    filter_fields = ("date", "title")
    filter_class = DateFilter

    def get_queryset(self):
        queryset = self.queryset
        self.filterset = self.filter_class(self.request.GET, queryset=queryset)
        return self.filterset.qs


class EventsCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthedUser]

    def post(self, request):
        data = request.data
        user_id = jwt.decode(request.COOKIES.get("jwt"), "secret", algorithms="HS256")["id"]
        data["organizer"] = user_id
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class EventsUpdateView(generics.UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthedUser]

    def update(self, request, partial, id):
        instance = self.queryset.get(id=id)
        serializer = self.serializer_class(instance, request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class EventsDeleteView(generics.DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthedUser]

    def delete(self, request, id):
        instance = self.queryset.get(id=id)
        resp = instance.delete()
        return Response(resp)


class EventsRetrieveView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthedUser]

    def get(self, request, id):
        instance = get_object_or_404(Event, id=id)
        serializer = self.serializer_class(instance)
        return Response(serializer.data)
