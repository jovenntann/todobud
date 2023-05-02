from django.urls import path
from .guests.id.todos.views import GuestsIdTodosAPIView

urlpatterns = [
    path('guests/<guest_id>/todos/', GuestsIdTodosAPIView.as_view()),
]
