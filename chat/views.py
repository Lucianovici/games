# -*- coding: utf-8 -*-
"""
Chat views.
"""
import uuid

from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from ws4redis.redis_store import RedisMessage
from ws4redis.publisher import RedisPublisher


class ChatRoomView(TemplateView):
    """
    View handling URL based private room.
    """
    template_name = 'chat/base.html'

    def get(self, request, *args, **kwargs):
        welcome = RedisMessage('Hello everybody')
        room_token = kwargs.get('token')
        RedisPublisher(facility=room_token, broadcast=True).publish_message(welcome)
        return super(ChatRoomView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ChatRoomView, self).get_context_data(**kwargs)
        context['token'] = kwargs.get('token')
        return context


class ChatRoomTokenView(TemplateView):
    """
    View generating unique tokens to be used in URL based private rooms.
    """

    def get(self, request, *args, **kwargs):
        room_token = uuid.uuid4().hex
        return redirect('chat-room', token=room_token)
