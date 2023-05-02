from django.urls import path

from .users.views import UsersAPIView
from .users.id.views import UsersIdAPIView
from .users.id.profile.views import UsersIdProfileAPIView

urlpatterns = [
    path('users', UsersAPIView.as_view()),
    path('users/<int:user_id>', UsersIdAPIView.as_view()),
    path('users/<int:user_id>/profile', UsersIdProfileAPIView.as_view()),
]
