from rest_framework import serializers

from appeal.models import *

class RequestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestedUser
        fields = ('id', 'telegram_id', 'first_name', 'last_name', 'group', 'type')
        extra_kwargs = {
            'id':{'read_only':True},
        }

class RequestedUserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestedUserMessage
        fields = ('id', 'requested_user', 'message', 'request_type')
        extra_kwargs = {
            'id':{'read_only':True}
        }