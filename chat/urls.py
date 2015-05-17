# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from django.contrib import admin

from .views import ChatRoomTokenView, ChatRoomView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^room/(?P<token>\w{32})$', ChatRoomView.as_view(), name='chat-room'),
    url(r'^new-room/$', ChatRoomTokenView.as_view(), name='chat-room-token'),
)
