from django.urls import path
from .guests.id.todos.views import GuestsIdTodosAPIView
from .guests.id.chats.views import GuestsIdChatsAPIView

urlpatterns = [
    path('guests/<guest_id>/todos/', GuestsIdTodosAPIView.as_view()),
    path('guests/<guest_id>/chats/', GuestsIdChatsAPIView.as_view()),
]
