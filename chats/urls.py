from django.urls import path
from . import views
app_name = "chats"

urlpatterns = [
    path("go/<int:host_pk>/<int:b_pk>", views.go_conversation, name='go')
]