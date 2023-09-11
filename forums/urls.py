from django.urls import path
from .views import ForumListCreate, ForumDetail, MessageListCreate, MessageDetail

urlpatterns = [
    path('forums/', ForumListCreate.as_view(), name='forum-list-create'),
    path('forums/<int:pk>/', ForumDetail.as_view(), name='forum-detail'),
    path('forums/<int:forum_id>/messages/', MessageListCreate.as_view(), name='message-list-create'),
    path('forums/<int:forum_id>/messages/<int:pk>/', MessageDetail.as_view(), name='message-detail'),
]
