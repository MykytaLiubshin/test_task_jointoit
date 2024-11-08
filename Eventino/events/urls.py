from django.urls import path
from events.views import EventsListView, EventsCreateView, EventsUpdateView, EventsDeleteView, EventsRetrieveView

urlpatterns = [
    path("events/", EventsListView.as_view()),
    path("create-event/", EventsCreateView.as_view()),
    path("update-event/<id>", EventsUpdateView.as_view()),
    path("delete-event/<id>", EventsDeleteView.as_view()),
    path("retrieve-event/<id>", EventsRetrieveView.as_view()),
]
